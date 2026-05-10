import unittest
from Operations.sort_eigen import sort_eigenpairs


class TestSortEigen(unittest.TestCase):
    def test_sort_eigenpairs_descending(self):
        eigenvalues = [1.0, 3.0, 2.0]
        eigenvectors = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]

        sorted_values, sorted_vectors = sort_eigenpairs(eigenvalues, eigenvectors)

        self.assertEqual(sorted_values, [3.0, 2.0, 1.0])
        self.assertEqual(
            sorted_vectors,
            [
                [0.0, 0.0, 1.0],
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
            ],
        )
