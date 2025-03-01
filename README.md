# PPEGuard.AI (SafetyKit Detection System)

This repository contains a real-time project for detecting safety helmets, gloves, dress code compliance, and shoes in an industrial environment using advanced computer vision techniques. The system is designed to enhance worker safety by monitoring compliance with PPE (Personal Protective Equipment) regulations.

🚀 **Current Status:**
- **Helmet detection** is fully implemented and functional.
- **Gloves, dress code, and shoes detection** are currently under development.

## Features
- **Real-time safety helmet detection** (Completed ✅)
- **Advanced deep learning-based computer vision techniques**
- **Scalability for various industrial settings**
- **High accuracy in detecting PPE compliance**
- **Future integration with IoT for automated alerts**

## Technologies Used
- **Programming Language:** Python
- **Frameworks/Libraries:**
  - OpenCV
  - TensorFlow/Keras
  - NumPy
- **Hardware Support:** Future compatibility with edge devices (e.g., Raspberry Pi, NVIDIA Jetson)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VathareVinayak/safety-detection-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd safety-detection-system
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure your camera or video feed is configured and accessible.
2. Run the helmet detection script:
   ```bash
   python helmet_detection.py
   ```
3. The system will process the video feed and highlight:
   - **Workers wearing helmets** (Green bounding box)
   - **Workers without helmets** (Red bounding box)

## Dataset
- Utilizes a publicly available safety helmet detection dataset.
- Data augmentation techniques applied to improve model performance.

## Model Training
1. Organize the dataset into labeled directories (e.g., `helmet` and `no_helmet`).
2. Train the model using the provided script:
   ```bash
   python train_model.py
   ```
3. Evaluate the model:
   ```bash
   python evaluate_model.py
   ```

## 🚧 Future Enhancements (Under Development)
- 🧤 *Gloves Detection*
- 👕 *Dress Code Compliance Detection*
- 👞 *Shoes Detection*
- 📡 *Integration with IoT for real-time monitoring & alerts*
- 🚀 *Deployment optimization for edge devices*
  
## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Open a pull request with detailed explanations.

## Acknowledgments
- OpenCV and TensorFlow for providing powerful computer vision tools.
- Dataset contributors for enabling the development of this project.

📢 Stay tuned for updates as we enhance PPEGuard.AI to detect more safety gear! 🚀

