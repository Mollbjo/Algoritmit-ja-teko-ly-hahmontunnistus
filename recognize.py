import Operations.model_io as model_io
import Operations.distance as distance
import Operations.Matrix as Matrix
import csv

def recognize_face(unknown_vector, mean_face, U_k_matrix, known_signatures):
    """
    Tunnistaa tuntemattoman kasvokuvan vertaamalla sitä tunnettuun malliin. Tämä funktio suorittaa seuraavat vaiheet:
    """
    # 1. Keskiarvon vähennys (Phi = Gamma - Psi)
    phi = [0.0] * len(unknown_vector)
    for i in range(len(unknown_vector)):
        phi[i] = unknown_vector[i] - mean_face[i]
        
    # 2. Muunna phi Matrix-olioksi (sarakevektori: 10304 riviä x 1 sarake)
    phi_matrix = Matrix.Matrix(len(phi), 1)
    for i in range(len(phi)):
        phi_matrix.data[i][0] = phi[i]
        
    # 3. Projektoi ominaiskasvoihin (Omega = U_k^T * Phi)
    U_k_transposed = U_k_matrix.transpose()
    omega_matrix = U_k_transposed.dot(phi_matrix)
    
    # Poimi tuloksena saatu 1D-signatuurilista
    unknown_signature = [omega_matrix.data[i][0] for i in range(omega_matrix.rows)]
    
    # 4. Etsi lähin osuma euklidisella etäisyydellä (lähimmän naapurin menetelmä)
    min_distance = float('inf')
    best_match_id = None
    
    for known_signature, subject_id in known_signatures:
        dist = distance.euclidean_distance(unknown_signature, known_signature)
        if dist < min_distance:
            min_distance = dist
            best_match_id = subject_id
            
    return best_match_id, min_distance

if __name__ == "__main__":
    print("Ladataan koulutettu malli...")
    mean_face, U_k, labeled_signatures = model_io.load_model()
    
    print("Ladataan testidata...")
    with open("data/testing_data.csv", "r") as f:
        reader = csv.reader(f)
        testing_data = list(reader)
        
    total_tests = len(testing_data)
    correct_predictions = 0
    
    print(f"Aloitetaan arviointi: {total_tests} aiemmin näkemätöntä kuvaa...\n")
    
    for index, raw_row in enumerate(testing_data):
        test_image_vector = [float(x) for x in raw_row]
        
        # Laske kuvalle todellinen kohteen tunniste.
        # Jokaisella henkilöllä on 3 testikuvaa, joten indeksit 0,1,2 kuuluvat kohteelle 1.
        # Indeksit 3,4,5 kuuluvat kohteelle 2 ja niin edelleen.
        actual_id = (index // 3) + 1
        
        # Suorita tunnistusalgoritmi.
        predicted_id, confidence_score = recognize_face(test_image_vector, mean_face, U_k, labeled_signatures)
        
        # Tarkista, oliko ennuste oikea.
        if predicted_id == actual_id:
            correct_predictions += 1
            # Valinnainen: tulosta oikein tunnistetut osumat reaaliaikaisen seurannan tueksi.
            # print(f"Oikein! Kohde {actual_id} tunnistettiin etäisyydellä {confidence_score:.2f}")
        else:
            # Virheiden tulostaminen auttaa näkemään, mikä hämmentää algoritmia.
            print(f"VIRHE: Odotettiin kohdetta {actual_id}, mutta ennustettiin kohde {predicted_id} (etäisyys: {confidence_score:.2f})")
            
    # Laske ja tulosta lopullinen tarkkuus.
    accuracy = (correct_predictions / total_tests) * 100
    
    print("\n" + "="*40)
    print("ARVIOINTI VALMIS")
    print("="*40)
    print(f"Oikein yhteensä: {correct_predictions} / {total_tests}")
    print(f"Kokonaistarkkuus: {accuracy:.2f}%")