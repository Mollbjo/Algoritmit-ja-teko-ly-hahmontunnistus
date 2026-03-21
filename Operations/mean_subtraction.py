from mean_face import mean_face_vector
import Matrix
import csv

def build_matrix(mean_face):
    """Rakentaa matriisin, jossa jokainen kolumni on training datan vektori, josta on vähennetty mean face
    vektori
    """
    with open("data/training_data.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)
        rows = len(mean_face)
        columns = len(data)
        matrix = Matrix.Matrix(rows, columns)

        for i in range(columns):
            vector = data[i]
            for j in range(rows):
                #Vähennetään kolumnista mean face vektori
                matrix.data[j][i] = float((float(vector[j]) - mean_face[j]))

        return matrix

build_matrix(mean_face_vector)

