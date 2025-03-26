# from fastapi import APIRouter
# from fastapi.responses import StreamingResponse
# import cv2
# import time

# stream_router = APIRouter(prefix="/stream", tags=["Live Stream"])

# def generate_frames():
#     # Open video capture: 0 uses the default webcam.
#     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#     if not cap.isOpened():
#         raise Exception("Cannot open camera")
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         # Encode the frame in JPEG format
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame_bytes = buffer.tobytes()
#         # Yield frame in byte format as part of a multipart response
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
#         # Control frame rate (approx 30 FPS)
#         time.sleep(0.033)
#     cap.release()

# @stream_router.get("/")
# def video_feed():
#     return StreamingResponse(
#         generate_frames(),
#         media_type="multipart/x-mixed-replace; boundary=frame"
#     )


from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import cv2
import time
from ultralytics import YOLO

stream_router = APIRouter(prefix="/stream", tags=["Live Stream"])

# Load your YOLO model from the models folder
model = YOLO(r"D:\#Safety Kit\Construction-Site-Safety-PPE-Detection\models\best.pt")

def generate_frames():
    # Open video capture: 0 uses the default webcam.
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        raise Exception("Cannot open camera")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Run inference on the frame
        results = model(frame)
        # Get the annotated frame (predictions drawn on the image)
        annotated_frame = results[0].plot()

        # Encode the annotated frame in JPEG format
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()
        
        # Yield frame in multipart format
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        
        # Control frame rate (approx 30 FPS)
        time.sleep(0.033)
    
    cap.release()

@stream_router.get("/")
def video_feed():
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
