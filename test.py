import Operations.Matrix as Matrix
import Operations.mean_subtraction as mean_subtraction
from Operations.mean_face import mean_face_vector
import Operations.jacobi_operation as jacobi_operation
import Operations.sort_eigen as sort_eigen
import Operations.normalize as normalize
import Operations.projection as projection
import Operations.model_io as model_io

print("Vektorin pituus:", len(mean_face_vector))
matrix = mean_subtraction.build_matrix(mean_face_vector)
print("Matriisin koko:", matrix.rows, "x", matrix.columns)
matrix_transposed = Matrix.Matrix.transpose(matrix)
print("Transponoidun matriisin koko:", matrix_transposed.rows, "x", matrix_transposed.columns)
matrix_L = matrix_transposed.dot(matrix)
print("L-matriisin koko:", matrix_L.rows, "x", matrix_L.columns)

eigenvalues, eigenvectors = jacobi_operation.get_eigen_jacobi(matrix_L.data)

sorted_vals, sorted_vecs = sort_eigen.sort_eigenpairs(eigenvalues, eigenvectors)

V_matrix = Matrix.Matrix(len(sorted_vecs), len(sorted_vecs[0]))
V_matrix.data = sorted_vecs

U_matrix = matrix.dot(V_matrix)

print("Varsinaisen ominaiskasvomatriisin koko:", U_matrix.rows, "x", U_matrix.columns)

final_eigenfaces = normalize.normalize_eigenfaces(U_matrix)

print("Normalisointi valmis. Projektio voidaan aloittaa.")
K = 50

U_k = projection.get_top_k_eigenfaces(final_eigenfaces, K)
print(f"Poimittiin {K} tärkeintä ominaiskasvoa.")

training_signatures_matrix = projection.project_faces(U_k, matrix)
print(f"Luotiin signatuurimatriisi: {training_signatures_matrix.rows} x {training_signatures_matrix.columns}")

labeled_training_signatures = projection.extract_labeled_signatures(training_signatures_matrix)
print(f"Merkittiin onnistuneesti {len(labeled_training_signatures)} opetussignatuuria.")

model_io.save_model(mean_face_vector, U_k, labeled_training_signatures)