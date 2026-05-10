import unittest
from Operations.Matrix import Matrix
from Operations.reconstruction import calculate_reconstruction_error


class TestReconstruction(unittest.TestCase):
    def test_reconstruction_error_zero_for_identity(self):
        U_k = Matrix(2, 2)
        U_k.data = [[1.0, 0.0], [0.0, 1.0]]

        original_phi = [1.0, 2.0]
        signature = [1.0, 2.0]

        error = calculate_reconstruction_error(original_phi, signature, U_k)

        self.assertAlmostEqual(error, 0.0)

    def test_reconstruction_error_matches_distance(self):
        U_k = Matrix(2, 1)
        U_k.data = [[0.0], [0.0]]

        original_phi = [3.0, 4.0]
        signature = [0.0]

        error = calculate_reconstruction_error(original_phi, signature, U_k)

        self.assertAlmostEqual(error, 5.0)
