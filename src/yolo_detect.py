from pathlib import Path
import pandas as pd
from ultralytics import YOLO

MODEL = YOLO("yolov8n.pt")

IMAGE_DIR = Path("data/raw/images")
OUT_DIR = Path("data/transformed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

rows = []

for channel_dir in IMAGE_DIR.iterdir():
    if not channel_dir.is_dir():
        continue

    for img in channel_dir.glob("*.jpg"):
        results = MODEL(img, verbose=False)
        for r in results:
            for box in r.boxes:
                rows.append({
                    "channel_name": channel_dir.name,
                    "image_name": img.name,
                    "label": r.names[int(box.cls)],
                    "confidence": float(box.conf)
                })

df = pd.DataFrame(rows)
df.to_csv(OUT_DIR / "image_detections.csv", index=False)
print("YOLO detections saved.")
