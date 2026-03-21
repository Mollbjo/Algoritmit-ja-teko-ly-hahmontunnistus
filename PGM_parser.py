import os
import csv

def load_data(dataset_path):
    training_data = []
    testing_data = []
    
    for folder_id in range(1, 41):
        folder_path = os.path.join(dataset_path, f"s{folder_id}")

        for image_id in range(1, 11):
            image_path = os.path.join(folder_path, f"{image_id}.pgm")

            image_vector = read_pgm(image_path)[0]

            if image_id < 8:
                training_data.append(image_vector)
            else:
                testing_data.append(image_vector)

    return training_data, testing_data

def write_data(training_data, testing_data):
    if not os.path.exists("data/training_data.csv"):
        with open("data/training_data.csv", "w") as f:
            for data_point in training_data:
                f.write(",".join(str(x) for x in data_point) + "\n")
    elif not os.path.exists("data/testing_data.csv"):
        with open("data/testing_data.csv", "w") as f:
            for data_point in testing_data:
                f.write(",".join(str(x) for x in data_point) + "\n")

def read_pgm(filepath):
    with open(filepath, "rb") as f:
        #Lukee PGM-tiedoston tyyppi
        file_type = f.readline().strip()
        if file_type != b'P5':
            raise ValueError("Tiedosto tyyppiä {0}, ei tuettu, tiedoston pitää olla tyyppiä P5".format(file_type))
        else:
        #Lukee ulottuvuudet
            line = f.readline()
            width, height = [int(i) for i in line.split()]
            #Lukee maksimi grayscale arvon
            max_gray = int(f.readline().strip())
            #Lukee kuvan binääri datan ja muuttaa sen listaksi kokonaislukuja skaalalla 0-255
            image_data = list(f.read())
            #Normalisoidaan data, jokaista pixeliä kohden
            normalized_data = [data_point / max_gray for data_point in image_data]

            return normalized_data, width, height
    
if __name__ == "__main__":
    #Esimerkki PGM-tiedoston lukemisesta
    path = "datasets/archive"
    if os.path.exists("datasets/archive"):
        training_data, testing_data = load_data(path)
        print("Training data size:", len(training_data))
        print("Testing data size:", len(testing_data))
        write_data(training_data, testing_data)
