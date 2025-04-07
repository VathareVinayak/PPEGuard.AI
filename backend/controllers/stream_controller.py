from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import cv2
import time
from ultralytics import YOLO

stream_router = APIRouter(prefix="/stream", tags=["Live Stream"])

# Load the YOLO model
model = YOLO(r"D:\#Safety Kit\Construction-Site-Safety-PPE-Detection\models\best.pt")

def generate_frames():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        raise RuntimeError("❌ Cannot open webcam.")

    print("✅ Camera opened, starting stream...")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ Failed to grab frame.")
                break

            # Run model inference
            results = model(frame)
            annotated_frame = results[0].plot()

            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            if not ret:
                print("⚠️ Frame encoding failed.")
                continue

            frame_bytes = buffer.tobytes()

            # Yield in multipart format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

            # Frame rate control
            time.sleep(0.033)  # ~30 FPS
    finally:
        cap.release()
        print("📷 Camera released.")

@stream_router.get("/")
def video_feed():
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
