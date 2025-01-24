# Safety Helmet Detection System

This repository contains a real-time project for detecting safety helmets in an industrial environment using computer vision techniques. The system ensures worker safety by monitoring compliance with helmet usage regulations in the workplace.

## Repository Link
[Safety Detection System](https://github.com/VathareVinayak/safety-detection-system.git)

## Features
- Real-time safety helmet detection.
- Uses advanced computer vision techniques.
- Scalable and adaptable to different industrial environments.
- High detection accuracy with support for multiple workers.

## Technologies Used
- **Programming Language**: Python
- **Frameworks/Libraries**: 
  - OpenCV
  - TensorFlow/Keras
  - NumPy
- **Hardware**: Optional support for edge devices (e.g., Raspberry Pi, NVIDIA Jetson)

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
2. Run the detection script:
   ```bash
   python helmet_detection.py
   ```
3. The system will process the video feed and highlight workers wearing or not wearing helmets in real time.

## Dataset
- Use a publicly available safety helmet detection dataset or create your own labeled dataset.
- Ensure proper data augmentation to improve model performance.

## Model Training
1. Prepare your dataset by organizing it into labeled directories (e.g., `helmet` and `no_helmet`).
2. Train the model using the provided training script:
   ```bash
   python train_model.py
   ```
3. Evaluate the model using:
   ```bash
   python evaluate_model.py
   ```

## Results
- The system highlights:
  - Workers wearing helmets (Green bounding box).
  - Workers without helmets (Red bounding box).

## Future Enhancements
- Add support for additional PPE detection (e.g., vests, gloves).
- Integrate with IoT devices for automated alerts.
- Optimize for deployment on edge devices.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Open a pull request detailing your changes.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- OpenCV and TensorFlow for providing powerful tools for computer vision.
- Dataset contributors for enabling this project.
