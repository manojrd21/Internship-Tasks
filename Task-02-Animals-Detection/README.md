# Project Title: Animal Detection Using YOLOv8 with GUI

## Objective:
To develop an **animal detection system** using the YOLOv8 object detection model that identifies animals from images or videos, highlights carnivorous animals in red, and displays the total count of carnivores detected via a popup message.

## Problem Statement:
Animal detection from visual data is critical for wildlife monitoring, security, and ecological studies. However, differentiating between carnivorous and non-carnivorous animals can be challenging. This project provides a solution by classifying and detecting animals while highlighting carnivores for further action.

## Scope of the Project:
- Accepts **image or video input** through a user-friendly GUI.
- Detects and classifies **88 different animal classes**.
- Highlights carnivorous animals in **red**.
- Displays a **popup message** with the number of carnivores detected.
- Saves processed outputs (annotated images/videos).

## Software and Hardware Requirements:

### Software Requirements:
- Python 3.10+
- Flask (Backend)
- PyTorch
- Ultralytics YOLOv8
- HTML, CSS, JavaScript (Frontend)

### Hardware Requirements:
- System with at least 4GB RAM
- GPU (CUDA-enabled) preferred for faster detection
- Modern browser (Chrome, Edge, Firefox)

## Dataset:
- **Name**: Custom Animals Dataset  
- **Link**: [Download Dataset](https://drive.google.com/drive/folders/15_akUUHFpXZwkoUDk05qD2-mCI56espN?usp=sharing)  
- **Description**: Dataset contains **88 classes** of animals, including carnivorous and non-carnivorous species.  

### Carnivorous Classes:
`Badger, Bat, Bear, Cat, Chimpanzee, Crow, Dog, Dolphin, Eagle, Fox, Hyena, Leopard, Lion, Lizard, Orangutan, Owl, Shark, Snake, Tiger, Wolf, Otter, Seal, Whale`

### Dataset Split:
- Training: 80%  
- Validation: 10%  
- Testing: 10%  

## Technologies Used:
- **Object Detection**: YOLOv8 (Ultralytics)
- **Framework**: Flask (Backend)
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualization**: OpenCV, Pillow

## Methodology:
1. **Input**: User uploads image/video through the GUI.
2. **Detection**: YOLOv8 model detects animals and classifies them.
3. **Carnivore Identification**: Carnivorous animals are highlighted in red.
4. **Output**: A popup message displays the number of carnivorous animals detected, and processed images/videos are saved in the output directory.

## System Architecture:
- **Frontend**: `index.html`, `style.css`, `script.js`
- **Backend**: `Flask (main.py)`
- **Model**: YOLOv8 trained model saved as `.pt` file
- **Utilities**: Class mapping and drawing utilities in `utils/`

## Project Structure
```bash
Task-2-Animals-Detection/
├── backend/
│ ├── outputs/
│ │ ├── detected_images/
│ │ └── detected_videos/
│ ├── utils/
│ │ ├── class_mapping.py
│ │ └── draw_utils.py
| |── uploads/
│ ├── detect.py
│ └── main.py
├── frontend/
│ ├── static/
│ │ ├── script.js
│ │ └── style.css
│ └── templates/
│   └── index.html
├── saved_model/
│ └── best.pt
├── testing_img_vid/
├── animals_detection_model.ipynb
├── requirements.txt
└── README.md
```

## Model Weights
Download the trained model weights from the link below:

[Download Model Weights](https://drive.google.com/drive/folders/1TzgZEYzX5DvkjVtlM4JgWA6DmR6SeOAl?usp=sharing)*

## Steps to Run the Project:

1. Clone the repository:
```bash
git clone <https://github.com/manojrd21/Internship-Tasks.git>
cd Task-2-Animals-Detection
```

2. Install Dependencies:
```bash
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
# Alternatively, install torch and related packages separately:
pip install torch==2.1.2+cpu torchvision==0.16.2+cpu torchaudio==2.1.2+cpu --index-url https://download.pytorch.org/whl/cpu
```

3. Start the Flask App:
```bash
python backend/main.py
```
4. Open the app in your browser and:
- Upload an image or video
- View detection results
- Pop-up will show carnivore count
- Processed output will be saved in backend/outputs/

## Requirements
The list of dependencies is in requirements.txt. Key libraries:
- flask
- flask-cors
- torch
- opencv-python
- numpy==1.24.4
- matplotlib
- ultralytics
- pillow

## Output
- Detected image/video saved in backend/outputs/
- Bounding boxes drawn around animals
- Carnivorous animals highlighted in red
- Pop-up message with carnivore count displayed in the GUI

## Limitations:
- Performance depends on input image/video quality.
- Real-time video streaming detection not implemented (only file-based).
- Carnivore identification limited to predefined classes.

## Future Scope:
- Implement real-time detection using webcams or IP cameras.
- Deploy system on the cloud for wider access.
- Extend classification to include endangered species tagging.

## Conclusion:
This project demonstrates the effectiveness of YOLOv8 for animal detection with a focus on carnivore identification. By providing an interactive GUI and clear visualization, it is suitable for wildlife monitoring, conservation, and security applications.

## Author:
Manoj Dhanawade
NULLCLASS Internship Task
