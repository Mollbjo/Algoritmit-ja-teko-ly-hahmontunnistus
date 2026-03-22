import os
import Operations.Matrix as Matrix
import Operations.mean_subtraction as mean_subtraction
from Operations.mean_face import mean_face_vector

print("vektori pituudella:", len(mean_face_vector))
matrix = mean_subtraction.build_matrix(mean_face_vector)
print("matriisi kooltaan:", matrix.rows, "x", matrix.columns)
matrix_transposed = Matrix.Matrix.transpose(matrix)
print("transponoitu matriisi kooltaan:", matrix_transposed.rows, "x", matrix_transposed.columns)
matrix_L = matrix_transposed.dot(matrix)
print("L matriisi kooltaan:", matrix_L.rows, "x", matrix_L.columns)
