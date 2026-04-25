import json
from . import Matrix

def save_model(mean_face, U_k_matrix, labeled_signatures, filepath="data/trained_model.json"):
    """
    Tallentaa oleelliset mallin komponentit JSON-muodossa. Tämä sisältää mean_face-vektorin, U_k-matriisin datan ja merkittyjen signatuurien listan.
    """

    model_data = {
        "mean_face": mean_face,
        "eigenfaces": U_k_matrix.data,
        "signatures": labeled_signatures
    }
    
    with open(filepath, "w") as f:
        json.dump(model_data, f)
    print(f"Malli tallennettu onnistuneesti {filepath}")

def load_model(filepath="data/trained_model.json"):
    """
    Lataa mallin komponentit JSON-tiedostosta. Palauttaa mean_face-vektorin, U_k-matriisin ja merkittyjen signatuurien listan.
    """
    with open(filepath, "r") as f:
        model_data = json.load(f)
        
    mean_face = model_data["mean_face"]
    labeled_signatures = model_data["signatures"]
    

    eigenfaces_data = model_data["eigenfaces"]
    rows = len(eigenfaces_data)
    cols = len(eigenfaces_data[0])
    
    U_k_matrix = Matrix.Matrix(rows, cols)
    U_k_matrix.data = eigenfaces_data
    
    return mean_face, U_k_matrix, labeled_signatures