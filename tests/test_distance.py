import unittest
from Operations.distance import euclidean_distance


class TestDistance(unittest.TestCase):
    def test_euclidean_distance_returns_correct_value(self):
        self.assertAlmostEqual(euclidean_distance([0.0, 0.0], [3.0, 4.0]), 5.0)

    def test_euclidean_distance_raises_on_length_mismatch(self):
        with self.assertRaises(ValueError):
            euclidean_distance([1.0, 2.0], [1.0])
