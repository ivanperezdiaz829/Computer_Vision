from scipy.spatial import distance as dist # Usiamo scipy.spatial.distance per la distanza euclidea

# 1. Funzione per calcolare l'Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    # Calcola la distanza Euclidea tra le 2 coppie di landmark verticali dell'occhio
    # A = distanza tra punto 2 e punto 6 (verticale, sinistra)
    A = dist.euclidean(eye[1], eye[5])
    # B = distanza tra punto 3 e punto 5 (verticale, destra)
    B = dist.euclidean(eye[2], eye[4])
    
    # Landmark orizzontali dell'occhio
    # C = distanza tra punto 1 e punto 4 (orizzontale)
    C = dist.euclidean(eye[0], eye[3])
    
    # Calcola l'Eye Aspect Ratio (EAR)
    # valore alto quando l'occhi e` aperto
    ear = (A + B) / (2.0 * C)
    return ear

# 2. Definizione degli indici dlib per gli occhi (68-point landmark)
# Occhio destro (dalla prospettiva dell'utente, sinistro nell'immagine)
R_START, R_END = 42, 48 # Estrae i sei punti
# Occhio sinistro (dalla prospettiva dell'utente, destro nell'immagine)
L_START, L_END = 36, 42