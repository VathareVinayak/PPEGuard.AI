# from fastapi import APIRouter, Depends, UploadFile, File
# from sqlalchemy.orm import Session
# from ..models.database import get_db
# from ..services.detection_service import save_detection, get_all_detections, get_detections_by_category
# from ..utils.image_uploader import upload_image_to_imgbb
# from ultralytics import YOLO
# import shutil
# import os
# import uuid

# router = APIRouter()
# model = YOLO("models/best.pt")  # Load YOLO model

# def classify_labels(labels):
#     for label in labels:
#         if label.startswith("NO-"):
#             return "not_wearing"
#     return "wearing"

# @router.post("/upload/")
# async def upload_and_detect(file: UploadFile = File(...), db: Session = Depends(get_db)):
#     filename = f"{uuid.uuid4()}.jpg"
#     file_path = f"temp/{filename}"
#     os.makedirs("temp", exist_ok=True)

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     results = model(file_path)
#     labels = results[0].names
#     detected_items = [results[0].names[int(cls)] for cls in results[0].boxes.cls]
#     category = classify_labels(detected_items)
#     image_url = upload_image_to_imgbb(file_path)

#     os.remove(file_path)

#     detection = save_detection(db, image_url, category, ", ".join(detected_items))
#     return {
#         "category": category,
#         "image_url": image_url,
#         "detected_items": detected_items
#     }

# @router.get("/detections/")
# def all_detections(db: Session = Depends(get_db)):
#     return get_all_detections(db)

# @router.get("/detections/{category}")
# def detections_by_category(category: str, db: Session = Depends(get_db)):
#     return get_detections_by_category(db, category)


from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from ..models.database import get_db
from ..services.detection_service import save_detection, get_all_detections, get_detections_by_category
from ..utils.image_uploader import upload_image_to_imgbb
from ultralytics import YOLO
import shutil
import os
import uuid

router = APIRouter()
model = YOLO("models/best.pt")  # Load YOLO model

def classify_labels(labels):
    for label in labels:
        if label.upper().startswith("NO-"):
            return "not_wearing"
    return "wearing"

@router.post("/upload/")
async def upload_and_detect(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Save uploaded image to temp folder
    filename = f"{uuid.uuid4()}.jpg"
    file_path = os.path.join("temp", filename)
    os.makedirs("temp", exist_ok=True)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run YOLOv8 detection
    results = model(file_path)
    detected_items = []

    for result in results:
        detected_items += [model.names[int(cls)] for cls in result.boxes.cls]

    # Classify image: wearing or not_wearing
    category = classify_labels(detected_items)

    # Upload image to ImgBB
    image_url = upload_image_to_imgbb(file_path)

    # Clean up temp image
    os.remove(file_path)

    # Save detection to DB
    detection = save_detection(
        db,
        image_url=image_url,
        category=category,
        detected_items=", ".join(detected_items)
    )

    return {
        "category": category,
        "image_url": image_url,
        "detected_items": detected_items
    }

@router.get("/detections/")
def all_detections(db: Session = Depends(get_db)):
    return get_all_detections(db)

@router.get("/detections/{category}")
def detections_by_category(category: str, db: Session = Depends(get_db)):
    return get_detections_by_category(db, category)
