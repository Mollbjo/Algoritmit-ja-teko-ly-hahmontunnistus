import unittest
from Operations.Matrix import Matrix
from recognize import recognize_face


class TestRecognizeFace(unittest.TestCase):
    def test_recognize_face_returns_nearest_neighbor(self):
        mean_face = [0.0, 0.0]
        U_k = Matrix(2, 2)
        U_k.data = [[1.0, 0.0], [0.0, 1.0]]
        known_signatures = [([1.0, 2.0], 1), ([2.0, 2.0], 2)]

        predicted_id, score, is_face = recognize_face([1.0, 2.0], mean_face, U_k, known_signatures)

        self.assertTrue(is_face)
        self.assertEqual(predicted_id, 1)
        self.assertAlmostEqual(score, 0.0)

    def test_recognize_face_rejects_non_face(self):
        mean_face = [0.0, 0.0]
        U_k = Matrix(2, 1)
        U_k.data = [[0.0], [0.0]]
        known_signatures = [([0.0], 1)]

        predicted_id, score, is_face = recognize_face([100.0, 100.0], mean_face, U_k, known_signatures)

        self.assertFalse(is_face)
        self.assertIsNone(predicted_id)
        self.assertGreater(score, 24.0)
