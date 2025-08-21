# PPEGuard.AI 
## Detection System with YOLOv8 and Admin Dashboard

I build a **custom object detection system** using YOLOv8 to detect PPE (Personal Protective Equipment) in images and videos. Detected items are classified and displayed on an **Admin Dashboard** for monitoring compliance in real-time.
![PPEIMG](https://github.com/VathareVinayak/PPEGuard.AI/blob/main/output/output_yolov8n_100e/construction-safety.jpg)

---

## 🔹 Overview
This project leverages **YOLOv8** for custom object detection on PPE datasets. The system includes:

- **Detection & Classification:** Detects PPE items such as helmets, gloves, vests, goggles, masks, and boots, classifying whether each item is **Wearing** or **Not Wearing**.
- **Admin Dashboard:** Displays all detection results with images and classifications for easy monitoring.
- **Visualization & Reporting:** Includes confusion matrix, PR curves, and batch visualizations for training and validation sets.
---

## 🔹 Folder Structure

```
PPEGuard.AI
├───backend
│   ├───app
│   │   ├───controllers      # Detection and API logic
│   │   ├───models           # Database models (PostgreSQL)
│   │   ├───services         # Detection & classification services
│   │   ├───schemas          # Pydantic schemas
│   │   └───main.py          # FastAPI entrypoint
├───frontend
│   ├───templates            # HTML templates for dashboard
│   ├───static
│   │   ├───css              # Tailwind CSS files
│   │   └───js               # Optional JS files
├───data
│   ├───train
│   ├───valid
│   └───test
├───models
│   ├───yolov8n.pt           # Pre-trained YOLOv8 model
│   └───best.pt              # Custom trained model
├───output
├───results
│   ├───confusion_matrix.png
│   ├───PR_curve.png
│   └───batch_visualizations

````
- **data folder:** Contains training, validation, and test datasets along with `.yaml` config files.
- **models folder:** Stores pre-trained and custom-trained YOLOv8 models.
- **results folder:** Includes model predictions, confusion matrices, visualizations, and PR curves.
- **output folder:** Contains outputs after running the model for 100 epochs.
- **source_files folder:** Sample videos/images for evaluating the model.
- **backend folder**: FastAPI backend structured with MVC (controllers, models, services, schemas, main.py) for API and detection logic.
- **frontend folder:** HTML + Tailwind CSS frontend for Admin Dashboard and real-time visualization of detection results.
---

## 🔹 Training & Results

- **Model:** YOLOv8n (custom-trained)
- **Results:**  
  After training, the model produces:
  - Predictions on test images , Streaming Via Laptop Camera
  - Confusion matrix
  - PR curves
  - Batch visualizations

All detection outputs are automatically updated to the **Admin Dashboard**, showing:

- Detected PPE items
- Classification as **Wearing** or **Not Wearing**
- Images for visual confirmation
---

## 🔹 Admin Dashboard

The **Admin Dashboard** is a central feature of this project:

- Displays Classification of all detections.

**In Working**
- Allows easy filtering of detections by type or status
- Facilitates monitoring of safety compliance in workplaces

---

## 🔹 Set-Up Instructions 

1. Clone the repository:
```bash
git clone <repo-link>
cd <repo-folder>
````

2. Install dependencies:

```bash
pip install ultralytics
pip install -r requirements.txt
```
3.  Environment Variables & Setup

The project requires the following environment variables 

(add them to a .env file in the backend folder)
```bash
DATABASE_URL=YOUR_DATABASE_KEY
SECRET_KEY=YOUR_SECRET_KEY
ALGORITHM=HS256 (I USED THIS ALGORITHM FOR HASHED PASSWORD)
IMGBB_API_KEY=ADD_YOUR_DB_KEY
```

3. Run the detection system:
```bash
uvicorn main:app --reload
```

4. Access the **Admin Dashboard** to view classified detections.
```bash
http://127.0.0.1:8000/stream
```

---

## 🔹 Acknowledgements

* **Ultralytics YOLOv8** for the object detection framework
* Kaggle for GPU resources
* Dataset contributors for PPE images


