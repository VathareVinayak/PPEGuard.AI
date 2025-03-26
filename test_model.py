from ultralytics import YOLO


# Load the trained model
model = YOLO("models/best.pt")

results = model(r"D:\#Safety Kit\Construction-Site-Safety-PPE-Detection\data\test\images\Movie-on-10-31-22-at-10_08-AM_mov-24_jpg.rf.95ec6998880e7bb081f76b11a5e978e9.jpg", show=True)


for r in results:
    r.show()  # Displays the image with detections
