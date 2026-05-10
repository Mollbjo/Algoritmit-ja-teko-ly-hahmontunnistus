import os
import tempfile
import unittest

from Operations import model_io
from Operations.Matrix import Matrix


class TestModelIO(unittest.TestCase):
    def test_save_and_load_roundtrip(self):
        mean_face = [0.1, 0.2]
        U_k = Matrix(2, 1)
        U_k.data = [[0.3], [0.4]]
        signatures = [([0.5], 1), ([0.6], 2)]

        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "model.json")
            model_io.save_model(mean_face, U_k, signatures, filepath=path)
            loaded_mean, loaded_U_k, loaded_signatures = model_io.load_model(filepath=path)

        self.assertEqual(mean_face, loaded_mean)
        expected_loaded = [[[0.5], 1], [[0.6], 2]]
        self.assertEqual(loaded_signatures, expected_loaded)
        self.assertEqual(loaded_U_k.rows, 2)
        self.assertEqual(loaded_U_k.columns, 1)
        self.assertEqual(loaded_U_k.data, [[0.3], [0.4]])
