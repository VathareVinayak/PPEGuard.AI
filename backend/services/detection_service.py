import requests
from sqlalchemy.orm import Session
from models.detection_model import Detection
from models.database import get_db
from fastapi import APIRouter, Depends, UploadFile, File
from ultralytics import YOLO
import uuid
import os
from dotenv import load_dotenv

load_dotenv()
IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")

# Load YOLOv8 model 
model = YOLO(r"J:\Projects\#PPE Suit Detection\PPEGuard.AI\models\best.pt")


# Upload image to ImgBB
def upload_to_imgbb(image_path: str):
    with open(image_path, "rb") as f:
        response = requests.post(
            "https://api.imgbb.com/1/upload",
            params={"key": IMGBB_API_KEY},
            files={"image": f},
        )
    if response.status_code == 200:
        return response.json()["data"]["url"]
    else:
        raise Exception("Failed to upload to ImgBB")


# Run YOLO prediction, classify, upload, save to DB
def predict_and_save(db: Session, image_file):
    # Save temp image file
    filename = f"temp_{uuid.uuid4().hex}.jpg"
    with open(filename, "wb") as f:
        f.write(image_file.file.read())

    # Run detection
    results = model(filename)
    labels = []
    for r in results:
        labels += [model.names[int(cls)] for cls in r.boxes.cls]

    # Classification: wearing / not_wearing
    category = "wearing"
    for label in labels:
        if "NO-" in label.upper():
            category = "not_wearing"
            break

    # Upload to ImgBB
    image_url = upload_to_imgbb(filename)

    # Save to DB
    detected_items = ", ".join(labels)
    detection = Detection(
        image_url=image_url,
        category=category,
        detected_items=detected_items
    )
    db.add(detection)
    db.commit()
    db.refresh(detection)

    # Clean up temp file
    os.remove(filename)

    return detection


def save_detection(db: Session, image_url: str, category: str, detected_items: str):
    detection = Detection(
        image_url=image_url,
        category=category,
        detected_items=detected_items
    )
    db.add(detection)
    db.commit()
    db.refresh(detection)
    return detection

def get_all_detections(db: Session):
    return db.query(Detection).all()

def get_detections_by_category(db: Session, category: str):
    return db.query(Detection).filter(Detection.category == category).all()