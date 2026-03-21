import unittest
from unittest.mock import mock_open, patch

from PGM_parser import load_data, read_pgm, write_data


class TestMeanFace(unittest.TestCase):
    def test_calculate_mean_face_returns_column_means(self):
        csv_data = "1,2,3\n4,5,6\n7,8,9\n"

        with patch("builtins.open", mock_open(read_data=csv_data)):
            with patch("builtins.print"):
                from Operations.mean_face import calculate_mean_face

                mean_face = calculate_mean_face()

        self.assertEqual(mean_face, [4.0, 5.0, 6.0])