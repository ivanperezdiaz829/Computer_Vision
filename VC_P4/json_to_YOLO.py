import json, os

input_dir = r"C:/Users/ivanp/Desktop/Matriculas-20251029T150805Z-1-001/Matriculas_filtradas/labels"
output_dir = os.path.join(input_dir, "YOLO_LABELS")

os.makedirs(output_dir, exist_ok=True)

for f in os.listdir(input_dir):
    if f.endswith(".json"):
        path = os.path.join(input_dir, f)

        data = json.load(open(path, "r", encoding="utf-8"))

        img_w = data["imageWidth"]
        img_h = data["imageHeight"]

        out_txt = os.path.join(output_dir, f.replace(".json", ".txt"))

        with open(out_txt, "w") as out:
            for shape in data["shapes"]:
                label = shape["label"]
                pts = shape["points"]

                xs = [p[0] for p in pts]
                ys = [p[1] for p in pts]

                x1, x2 = min(xs), max(xs)
                y1, y2 = min(ys), max(ys)

                cx = ((x1 + x2) / 2.0) / img_w
                cy = ((y1 + y2) / 2.0) / img_h
                w  = (x2 - x1) / img_w
                h  = (y2 - y1) / img_h

                # solo 1 clase -> id = 0
                out.write(f"0 {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}\n")

print("DONE")
