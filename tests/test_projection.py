import unittest
from Operations.Matrix import Matrix
from Operations.projection import (
    extract_labeled_signatures,
    get_top_k_eigenfaces,
    project_faces,
)


class TestProjection(unittest.TestCase):
    def test_get_top_k_eigenfaces_truncates_columns(self):
        m = Matrix(2, 3)
        m.data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

        result = get_top_k_eigenfaces(m, 2)

        self.assertEqual(result.rows, 2)
        self.assertEqual(result.columns, 2)
        self.assertEqual(result.data, [[1.0, 2.0], [4.0, 5.0]])

    def test_get_top_k_eigenfaces_clamps_k(self):
        m = Matrix(1, 1)
        m.data = [[7.0]]

        result = get_top_k_eigenfaces(m, 5)

        self.assertEqual(result.rows, 1)
        self.assertEqual(result.columns, 1)
        self.assertEqual(result.data, [[7.0]])

    def test_project_faces_identity_returns_same_matrix(self):
        U_k = Matrix(2, 2)
        U_k.data = [[1.0, 0.0], [0.0, 1.0]]

        mean_subtracted = Matrix(2, 2)
        mean_subtracted.data = [[1.0, 2.0], [3.0, 4.0]]

        weights = project_faces(U_k, mean_subtracted)

        self.assertEqual(weights.data, [[1.0, 2.0], [3.0, 4.0]])

    def test_extract_labeled_signatures_assigns_subject_ids(self):
        weights = Matrix(2, 4)
        weights.data = [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]]

        labeled = extract_labeled_signatures(weights, images_per_person=2)

        expected = [
            ([1.0, 5.0], 1),
            ([2.0, 6.0], 1),
            ([3.0, 7.0], 2),
            ([4.0, 8.0], 2),
        ]
        self.assertEqual(labeled, expected)
