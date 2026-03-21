import os
import csv

def calculate_mean_face():
    with open("data/training_data.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    
        vector_length = len(data[0])

        mean_face = [0.0] * vector_length

        for row in data:
            for i in range(vector_length):
                mean_face[i] += float(row[i])
        mean_face = [x / len(data) for x in mean_face]
    return mean_face

mean_face_vector = calculate_mean_face()
print("vektori pituudella:", len(mean_face_vector))
print("Ensimmäiset kymmynen vektorin arvoa:", mean_face_vector[:10])


