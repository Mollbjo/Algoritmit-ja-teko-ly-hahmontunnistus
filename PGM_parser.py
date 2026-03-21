import os

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
    pgm_file = "datasets/archive/s1/1.pgm"
    if os.path.exists("datasets/archive/s1/1.pgm"):
        data, width, height = read_pgm(pgm_file)
        print("Kuvan leveys: {0}, korkeus: {1}".format(width, height))
        print("Normalisoitu data (ensimmäiset 10 pistettä):", data[:10])