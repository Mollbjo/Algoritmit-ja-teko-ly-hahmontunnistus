import os
import tempfile
import unittest
from unittest.mock import patch
from PGM_parser import load_data, read_pgm, write_data


class TestReadPgm(unittest.TestCase):
    def test_read_pgm_parses_valid_p5_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"P5\n2 2\n255\n\x00\x7f\xff\x40")
            temp_path = temp_file.name

        self.addCleanup(lambda: os.path.exists(temp_path) and os.remove(temp_path))

        normalized_data, width, height = read_pgm(temp_path)

        self.assertEqual(width, 2)
        self.assertEqual(height, 2)
        self.assertEqual(normalized_data, [0 / 255, 127 / 255, 255 / 255, 64 / 255])

    def test_read_pgm_raises_for_non_p5_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"P2\n2 2\n255\n0 127 255 64")
            temp_path = temp_file.name

        self.addCleanup(lambda: os.path.exists(temp_path) and os.remove(temp_path))

        with self.assertRaises(ValueError):
            read_pgm(temp_path)


class TestLoadData(unittest.TestCase):
    @patch("PGM_parser.read_pgm")
    def test_load_data_splits_training_and_testing(self, mock_read_pgm):
        mock_read_pgm.side_effect = lambda path: ([path], 1, 1)

        training_data, testing_data = load_data("test_dataset")

        self.assertEqual(len(training_data), 40 * 7)
        self.assertEqual(len(testing_data), 40 * 3)

        self.assertEqual(training_data[0], [os.path.join("test_dataset", "s1", "1.pgm")])
        self.assertEqual(training_data[-1], [os.path.join("test_dataset", "s40", "7.pgm")])
        self.assertEqual(testing_data[0], [os.path.join("test_dataset", "s1", "8.pgm")])
        self.assertEqual(testing_data[-1], [os.path.join("test_dataset", "s40", "10.pgm")])


class TestWriteData(unittest.TestCase):
    def test_write_data_writes_training_file_when_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            os.makedirs("data", exist_ok=True)
            self.addCleanup(lambda: os.chdir(old_cwd))

            write_data([[1, 2], [3, 4]], [[9, 8]])

            with open("data/training_data.csv", "r") as file:
                self.assertEqual(file.read(), "1,2\n3,4\n")

            self.assertFalse(os.path.exists("data/testing_data.csv"))

    def test_write_data_writes_testing_file_when_training_exists(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            os.makedirs("data", exist_ok=True)
            self.addCleanup(lambda: os.chdir(old_cwd))

            with open("data/training_data.csv", "w") as file:
                file.write("already,exists\n")

            write_data([[1, 2]], [[9, 8], [7, 6]])

            with open("data/testing_data.csv", "r") as file:
                self.assertEqual(file.read(), "9,8\n7,6\n")
