import cv2
import dlib
import numpy as np
import time
import math
from blink_detector_utils_ita import eye_aspect_ratio, R_START, L_START, R_END, L_END

# --- Setup ---

# EAR: Soglia sotto la quale l'occhio è considerato chiuso
EYE_AR_THRESH = 0.25 
# Numero di frame consecutivi in cui l'EAR deve essere sotto la soglia per considerare l'occhio chiuso
EYE_AR_CONSEC_FRAMES = 3

STAR_IMAGE_PATH = "star.png" 
STAR_SIZE_START = 20 # Dimensione iniziale della stellina
STAR_SIZE_END = 80 # Dimensione finale della stellina
STAR_LIFETIME = 1.0 # Durata della vita di una stellina in secondi
STAR_SPEED = 20 # Velocità di movimento con cui si allontana dal centro dell'occhio (pixel al secondo)

# Stato
active_stars = [] # Traccia le stelle attive e le loro proprieta` (posizione, tempo di inizio)

# Contatori e flag
COUNTER = 0 # Contatore per i frame chiusi
BLINKS = 0  # Contatore ammiccamenti totali
EFFECT_TIMER = 0 # Timer per mostrare l'effetto
EFFECT_DURATION = 1.0 # Durata dell'effetto in secondi

# Percorso al file del modello di landmark (dlib) che riconosce i 68 punti del volto 
# (DEVE ESSERE NELLA CARTELLA VC)
SHAPE_PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"

# --- Inizializzazione ---

# Carica l'immagine della stellina
try:
    # Carica l'immagine BGR (3 canali) ignorando l'alpha, per il blending semplificato
    star_img_orig = cv2.imread(STAR_IMAGE_PATH, cv2.IMREAD_COLOR) 
    
    if star_img_orig is None:
        raise FileNotFoundError(f"Impossibile caricare l'immagine: {STAR_IMAGE_PATH}")
    
    print(f"[INFO] Immagine stellina caricata.")
except FileNotFoundError as e:
    print(f"[ERRORE] {e}. Assicurati che 'star.png' sia nella cartella del progetto.")
    star_img_orig = None
except Exception as e:
    print(f"[ERRORE] Errore generico caricando la stellina: {e}")
    star_img_orig = None

# Inizializza i detector di dlib
print("[INFO] Caricamento del detector facciale e del predittore di landmark...")
detector = dlib.get_frontal_face_detector() # Posizione generale del volto
predictor = dlib.shape_predictor(SHAPE_PREDICTOR_PATH) # Landmark

# Inizializza la webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Errore: Impossibile aprire la webcam.")
    exit()

# --- Ciclo principale di rilevamento ---

print("[INFO] Avvio del ciclo video...")
time_start = time.time()

# Acquisizione del frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preelaborazione
    frame = cv2.flip(frame, 1) # Effetto specchio
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Conversione scala di grigi
    
    # Rettangoli intorno ai volti
    rects = detector(gray, 0)
    
    # Cicla su ogni volto rilevato
    for rect in rects:
        # Trova i 68 landmark facciali
        shape = predictor(gray, rect)
        
        # Converti i landmark di dlib in un array NumPy (x, y)
        points = np.array([(p.x, p.y) for p in shape.parts()], dtype="int")
        
        # Estrai le coordinate dei landmark per gli occhi
        leftEye = points[L_START:L_END]
        rightEye = points[R_START:R_END]
        
        # Calcola l'EAR per entrambi gli occhi
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        
        # Media dell'EAR per entrambi gli occhi
        ear = (leftEAR + rightEAR) / 2.0
        
        # Visualizza i contorni degli occhi
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

# --- Logica di animazione ---
      
        if ear < EYE_AR_THRESH:
            # L'occhio è chiuso
            COUNTER += 1
            
        else:
            # L'occhio è aperto
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                BLINKS += 1
                
                # Genera le stelline al blink
                if star_img_orig is not None:
                    # Posizione iniziale per le stelline (vicino agli occhi)
                    # Usa le medie delle posizioni degli occhi per una posizione più precisa
                    le_center = np.mean(leftEye, axis=0).astype(int)
                    re_center = np.mean(rightEye, axis=0).astype(int)

                    # Aggiungi due stelline (una per occhio)
                    active_stars.append({
                        'start_time': time.time(),
                        'x': le_center[0], 'y': le_center[1], # Posizione occhio sinistro
                        'initial_pos': le_center
                    })
                    active_stars.append({
                        'start_time': time.time(),
                        'x': re_center[0], 'y': re_center[1], # Posizione occhio destro
                        'initial_pos': re_center
                    })
                # -----------------------------------
                
            # Reset del contatore
            COUNTER = 0

    # Applicazione dell'effetto stelline
    current_time = time.time()
    stars_to_keep = []

    for star in active_stars:
        elapsed_time = current_time - star['start_time']

        if elapsed_time < STAR_LIFETIME:
            # Calcola la dimensione attuale e l'opacità
            scale_factor = elapsed_time / STAR_LIFETIME # Percentuale di completamento dell'animazione normalizzata tra 0 e 1
            current_size = int(STAR_SIZE_START + (STAR_SIZE_END - STAR_SIZE_START) * scale_factor)
            alpha = 1.0 - scale_factor # Opacità basata sul tempo

            # Calcolo della posizione
            dir_x = (star['x'] - star['initial_pos'][0])
            dir_y = (star['y'] - star['initial_pos'][1])
            if dir_x == 0 and dir_y == 0:
                dir_x = 1
            
            magnitude = math.sqrt(dir_x**2 + dir_y**2)
            norm_dir_x, norm_dir_y = (dir_x / magnitude, dir_y / magnitude) if magnitude > 0 else (0, -1)
            
            move_distance = STAR_SPEED * elapsed_time
            new_x = int(star['initial_pos'][0] + norm_dir_x * move_distance)
            new_y = int(star['initial_pos'][1] + norm_dir_y * move_distance)

            # Ridimensiona l'immagine
            if star_img_orig is not None:
                resized_star = cv2.resize(star_img_orig, (current_size, current_size), interpolation=cv2.INTER_LINEAR)

                # Calcola le coordinate per l'overlay (ritaglio semplice)
                x1 = new_x - current_size // 2
                y1 = new_y - current_size // 2
                x2 = x1 + current_size
                y2 = y1 + current_size

                # Calcola i limiti di ritaglio del frame (assicurati che sia nei bordi)
                y1_frame = max(0, y1)
                x1_frame = max(0, x1)
                y2_frame = min(frame.shape[0], y2)
                x2_frame = min(frame.shape[1], x2)

                # Calcola i limiti di ritaglio della stellina
                y1_star_img = y1_frame - y1
                x1_star_img = x1_frame - x1
                y2_star_img = y1_star_img + (y2_frame - y1_frame)
                x2_star_img = x1_star_img + (x2_frame - x1_frame)

                # Estrai le ROI (regioni di interesse)
                roi_frame = frame[y1_frame:y2_frame, x1_frame:x2_frame].astype(np.float32)
                roi_star = resized_star[y1_star_img:y2_star_img, x1_star_img:x2_star_img].astype(np.float32)

                # sfondo * (1 - opacità) + oggetto * opacità
                blended_roi = roi_frame * (1.0 - alpha) + roi_star * alpha
                
                # Scrivi il risultato nel frame
                frame[y1_frame:y2_frame, x1_frame:x2_frame] = blended_roi.astype(np.uint8)
                
                stars_to_keep.append(star)
        
        active_stars = stars_to_keep # Aggiorna la lista delle stelline attive

# --- Uscita e pulizia

    # Mostra il frame
    cv2.imshow("Blink Filter", frame)
    
    # Esci premendo 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Pulizia
cap.release()
cv2.destroyAllWindows()