import math

def euclidean_distance(signature1, signature2):
    """
    Laskee euklidisen etäisyyden kahden signatuurin välillä. Signatuurien on oltava samaa pituutta.
    """
    if len(signature1) != len(signature2):
        raise ValueError("Signatuurien pituuden on oltava sama vertailua varten.")
        
    distance_sq = 0.0
    for i in range(len(signature1)):
        distance_sq += (signature1[i] - signature2[i]) ** 2
        
    return math.sqrt(distance_sq)