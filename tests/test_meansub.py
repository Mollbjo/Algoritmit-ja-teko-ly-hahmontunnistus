import unittest
from unittest.mock import mock_open, patch
from Operations.mean_subtraction import build_matrix

class TestMeanSubtraction(unittest.TestCase):
    def test_build_matrix_subtracts_mean_and_transposes_to_columns(self):
        csv_data = "3,5,7\n6,8,10\n"
        mean_face = [1.0, 2.0, 3.0]

        with patch("builtins.open", mock_open(read_data=csv_data)):
            
            matrix = build_matrix(mean_face)

        self.assertEqual(matrix.rows, 3)
        self.assertEqual(matrix.columns, 2)
        self.assertEqual(matrix.data[0][0], 2.0)
        self.assertEqual(matrix.data[1][0], 3.0)
        self.assertEqual(matrix.data[2][0], 4.0)
        
        self.assertEqual(matrix.data[0][1], 5.0)
        self.assertEqual(matrix.data[1][1], 6.0)
        self.assertEqual(matrix.data[2][1], 7.0)