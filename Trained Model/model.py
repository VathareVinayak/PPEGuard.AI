#imported Nessesary Libraries
import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import cvzone
from PIL import Image
import tempfile
import requests
from io import BytesIO

# Load YOLOv8 model
model = YOLO("best.pt")  # Ensure your model path is correct
names = model.model.names

# Streamlit app layout
st.title('Object Detection with YOLOv8')
st.write("This app allows image, video, and webcam-based object detection.")

# Sidebar for file upload
st.sidebar.header("Upload Image or Video File")
file = st.sidebar.file_uploader("Upload file", type=["jpg", "jpeg", "png", "mp4"])

# Paste Image/Video URL
st.sidebar.header("Paste YouTube or Image URL")
url_input = st.sidebar.text_input("Paste a link...")

# Try webcam detection
use_webcam = st.sidebar.button("Try With Webcam")

# Frame placeholder
frame_placeholder = st.empty()
result_placeholder = st.empty()

# Function to process images
def process_image(image):
    frame = np.array(image)
    results = model.track(frame, persist=True)
    detected_classes = []
    if results[0].boxes is not None and results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.int().cpu().tolist()
        class_ids = results[0].boxes.cls.int().cpu().tolist()
        track_ids = results[0].boxes.id.int().cpu().tolist()
        confidences = results[0].boxes.conf.cpu().tolist()
        for box, class_id, track_id, conf in zip(boxes, class_ids, track_ids, confidences):
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f'{names[class_id]} {conf:.0%}'
            cvzone.putTextRect(frame, label, (x1, y1), 1, 1)
            detected_classes.append(names[class_id])
    return frame, detected_classes

# Process uploaded image or video
if file:
    if file.type.startswith("image"):
        image = Image.open(file)
        frame, detected_classes = process_image(image)
        frame_placeholder.image(frame, channels="RGB", use_column_width=True)
        result_placeholder.write(f"Detected objects: {', '.join(set(detected_classes))}")
    elif file.type.startswith("video"):
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())
        cap = cv2.VideoCapture(tfile.name)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame, detected_classes = process_image(frame)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)
            result_placeholder.write(f"Detected objects: {', '.join(set(detected_classes))}")
        cap.release()

# Process image from URL
if url_input:
    try:
        response = requests.get(url_input, stream=True)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            frame, detected_classes = process_image(image)
            frame_placeholder.image(frame, channels="RGB", use_column_width=True)
            result_placeholder.write(f"Detected objects: {', '.join(set(detected_classes))}")
        else:
            st.write("Error: Unable to load image from URL.")
    except Exception as e:
        st.write(f"Error: {e}")

# Webcam live detection
if use_webcam:
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame, detected_classes = process_image(frame)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)
        result_placeholder.write(f"Detected objects: {', '.join(set(detected_classes))}")
    cap.release()
    cv2.destroyAllWindows()
