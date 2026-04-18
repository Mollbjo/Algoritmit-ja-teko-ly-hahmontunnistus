import unittest
import math
from Operations.jacobi_operation import get_eigen_jacobi

class TestJacobiOperation(unittest.TestCase):
    def test_get_eigen_jacobi_returns_correct_eigenvalues(self):
        
        L = [[2.0, 1.0], [1.0, 2.0]]
        
        eigenvalues, eigenvectors = get_eigen_jacobi(L)
        
        self.assertEqual(len(eigenvalues), 2)
        has_three = any(math.isclose(val, 3.0, abs_tol=1e-5) for val in eigenvalues)
        has_one = any(math.isclose(val, 1.0, abs_tol=1e-5) for val in eigenvalues)
        
        self.assertTrue(has_three)
        self.assertTrue(has_one)
        
        self.assertEqual(len(eigenvectors), 2)
        self.assertEqual(len(eigenvectors[0]), 2)