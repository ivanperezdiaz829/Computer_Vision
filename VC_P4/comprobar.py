import os

# rutas
images_dir = r"C:/Users/ivanp/Desktop/CarPlates/TGC_RBNW/val/images"
labels_dir = r"C:/Users/ivanp/Desktop/CarPlates/TGC_RBNW/val/labels"

# obtener nombres sin extensión
image_files = set(os.path.splitext(f)[0] for f in os.listdir(images_dir) if f.lower().endswith((".jpg",".png",".jpeg")))
label_files = set(os.path.splitext(f)[0] for f in os.listdir(labels_dir) if f.lower().endswith(".txt"))

# labels sin imagen
labels_sin_imagen = label_files - image_files
if labels_sin_imagen:
    print("Labels SIN imagen correspondiente:")
    for f in labels_sin_imagen:
        print(f)
else:
    print("Todos los labels tienen su imagen correspondiente ✅")

# imágenes sin label
imagenes_sin_label = image_files - label_files
if imagenes_sin_label:
    print("\nImágenes SIN label correspondiente:")
    for f in imagenes_sin_label:
        print(f)
else:
    print("\nTodas las imágenes tienen su label correspondiente ✅")
