import unittest
from Operations.Matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_initialization(self):
        matrix = Matrix(2, 3)
        self.assertEqual(matrix.rows, 2)
        self.assertEqual(matrix.columns, 3)
        self.assertEqual(matrix.data, [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])

    def test_add_matrices(self):
        m1 = Matrix(2, 2)
        m1.data = [[1.0, 2.0], [3.0, 4.0]]
        m2 = Matrix(2, 2)
        m2.data = [[5.0, 6.0], [7.0, 8.0]]
        
        result = m1.add(m2)
        self.assertEqual(result.data, [[6.0, 8.0], [10.0, 12.0]])

    def test_subtract_matrices(self):
        m1 = Matrix(2, 2)
        m1.data = [[5.0, 6.0], [7.0, 8.0]]
        m2 = Matrix(2, 2)
        m2.data = [[1.0, 2.0], [3.0, 4.0]]
        
        result = m1.subtract(m2)
        self.assertEqual(result.data, [[4.0, 4.0], [4.0, 4.0]])

    def test_dot_product_optimized(self):
        m1 = Matrix(2, 3)
        m1.data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
        m2 = Matrix(3, 2)
        m2.data = [[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]]
        
        result = m1.dot(m2)
        self.assertEqual(result.rows, 2)
        self.assertEqual(result.columns, 2)
        self.assertEqual(result.data, [[58.0, 64.0], [139.0, 154.0]])

    def test_dot_product_raises_value_error_on_mismatch(self):
        m1 = Matrix(2, 2)
        m2 = Matrix(3, 3)
        with self.assertRaises(ValueError):
            m1.dot(m2)

    def test_transpose(self):
        m = Matrix(2, 3)
        m.data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
        
        transposed = m.transpose()
        self.assertEqual(transposed.rows, 3)
        self.assertEqual(transposed.columns, 2)
        self.assertEqual(transposed.data, [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]])

    def test_elementwise_multiplication(self):
        m1 = Matrix(2, 2)
        m1.data = [[1.0, 2.0], [3.0, 4.0]]
        m2 = Matrix(2, 2)
        m2.data = [[2.0, 3.0], [4.0, 5.0]]

        result = m1.elementwise_multiplication(m2)

        self.assertEqual(result.data, [[2.0, 6.0], [12.0, 20.0]])

    def test_map_applies_function(self):
        m = Matrix(2, 2)
        m.data = [[1.0, 2.0], [3.0, 4.0]]

        result = m.map(lambda value: value + 1.0)

        self.assertEqual(result.data, [[2.0, 3.0], [4.0, 5.0]])