import Operations.model_io as model_io
import Operations.distance as distance
import Operations.Matrix as Matrix
import Operations.reconstruction as reconstruction
import PGM_parser
import sys

def recognize_face(unknown_vector, mean_face, U_k_matrix, known_signatures):
    # 1. Keskiarvon vähennys (Phi)
    phi = [0.0] * len(unknown_vector)
    for i in range(len(unknown_vector)):
        phi[i] = unknown_vector[i] - mean_face[i]
        
    # 2. Muutetaan phi Matrix-olioksi
    phi_matrix = Matrix.Matrix(len(phi), 1)
    for i in range(len(phi)):
        phi_matrix.data[i][0] = phi[i]
        
    # 3. Projisoidaan ominaisavaruuteen (Omega)
    U_k_transposed = U_k_matrix.transpose()
    omega_matrix = U_k_transposed.dot(phi_matrix)
    unknown_signature = [omega_matrix.data[i][0] for i in range(omega_matrix.rows)]
    
    # KASVO / EI KASVO -TARKISTUS
    reconstruction_error = reconstruction.calculate_reconstruction_error(phi, unknown_signature, U_k_matrix)
    
    # Asetetaan empiirisesti testattu kynnysarvo
    FACE_THRESHOLD = 24.0 
    
    if reconstruction_error > FACE_THRESHOLD:
        return None, reconstruction_error, False # Ei ole kasvo
        
    # 4. Etsitään lähin osuma (jos kyseessä on kasvo)
    min_distance = float('inf')
    best_match_id = None
    for known_signature, subject_id in known_signatures:
        dist = distance.euclidean_distance(unknown_signature, known_signature)
        if dist < min_distance:
            min_distance = dist
            best_match_id = subject_id
            
    return best_match_id, min_distance, True # On kasvo

if __name__ == "__main__":
    print(" EIGENFACE - KASVOJENTUNNISTUS")
    
    # Kysytään käyttäjältä kuvan polku
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = input("Syötä analysoitavan PGM-kuvan polku (esim. ei_kasvo.pgm): ")

    try:
        print("\nLadataan kuvaa ja mallia...")
        image_pixels, w, h = PGM_parser.read_pgm(image_path)
        mean_face, U_k, labeled_signatures = model_io.load_model()
        
        print("Analysoidaan kuvaa...\n")
        predicted_id, score, is_face = recognize_face(image_pixels, mean_face, U_k, labeled_signatures)
        
        if not is_face:
            print("TULOS: KUVASSA EI OLE IHMISKASVOA.")
            print(f"Syy: Kuvan matemaattinen rakenne poikkeaa liikaa ihmiskasvoista.")
            print(f"(Rekonstruktiovirhe: {score:.2f} | Sallittu raja: 24.00)")
        else:
            print("TULOS: KUVASSA ON IHMISKASVO!")
            print(f"Ennustettu henkilö (ID): {predicted_id}")
            print(f"(Luottamus/Etäisyys: {score:.2f})")
            print(f"(Rekonstruktiovirhe: {score:.2f} | Sallittu raja: 24.00)")
        
    except FileNotFoundError:
        print(f"Virhe: Tiedostoa '{image_path}' ei löytynyt!")
    except ValueError as e:
        print(f"Virhe kuvan lukemisessa: {e}")