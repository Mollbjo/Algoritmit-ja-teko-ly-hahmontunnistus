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

def read_pgm(filename):
    """
    Lukee P5-tyyppisen PGM-tiedoston ja palauttaa normalisoidut pikselit sekä mitat.
    Ohittaa automaattisesti #-alkuiset kommenttirivit.
    """
    with open(filename, 'rb') as f:
        # 1. Tarkistetaan "Magic Number" (P5)
        magic_number = f.readline().strip()
        if magic_number != b'P5':
            raise ValueError(f"Tiedosto ei ole P5 PGM -muodossa: {magic_number}")
            
        # Apufunktio, joka lukee seuraavan rivin, mutta hyppää kommenttien yli
        def read_next_valid_line():
            while True:
                line = f.readline()
                if not line.startswith(b'#'):
                    return line

        # 2. Luetaan leveys ja korkeus (ohittaen mahdolliset GIMPin kommentit)
        dimensions_line = read_next_valid_line()
        width, height = [int(i) for i in dimensions_line.split()]
        
        # 3. Luetaan maksimiarvo (yleensä 255)
        maxval_line = read_next_valid_line()
        maxval = int(maxval_line.strip())
        
        # 4. Luetaan pikselidata ja normalisoidaan (0.0 - 1.0)
        pixel_data = []
        # Luetaan tarkalleen width * height määrä tavuja
        raw_data = f.read(width * height)
        for byte in raw_data:
            pixel_data.append(byte / maxval)
            
        return pixel_data, width, height
    
if __name__ == "__main__":
    # Esimerkki PGM-tiedoston lukemisesta.
    path = "datasets/archive"
    if os.path.exists("datasets/archive"):
        training_data, testing_data = load_data(path)
        print("Opetusdatan koko:", len(training_data))
        print("Testidatan koko:", len(testing_data))
        write_data(training_data, testing_data)
