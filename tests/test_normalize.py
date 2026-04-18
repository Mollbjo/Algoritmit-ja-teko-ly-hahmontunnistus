import unittest
from Operations.Matrix import Matrix
from Operations.normalize import normalize_eigenfaces

class TestNormalize(unittest.TestCase):
    def test_normalize_eigenfaces_scales_to_unit_length(self):
        
        m = Matrix(3, 1)
        m.data = [[3.0], [0.0], [4.0]]
        
        normalized_m = normalize_eigenfaces(m)
        
        self.assertAlmostEqual(normalized_m.data[0][0], 0.6) # 3/5
        self.assertAlmostEqual(normalized_m.data[1][0], 0.0) # 0/5
        self.assertAlmostEqual(normalized_m.data[2][0], 0.8) # 4/5