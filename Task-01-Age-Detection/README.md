# Project Title: Age Detection Using Pretrained CNN on UTKFace Dataset

## Objective:
To develop an **age prediction system** using a fine-tuned pretrained CNN model on the UTKFace dataset. The model predicts the age of a person from a facial image and evaluates performance using accuracy, confusion matrix, precision, and recall.

## Problem Statement:
Age prediction from facial images is challenging due to variations in lighting, pose, and facial expressions. This project uses a robust CNN architecture to accurately predict age while leveraging transfer learning for improved performance.

## Scope of the Project:
- Predicts age from facial images using a deep learning model.
- Evaluates performance using standard metrics (Accuracy, Precision, Recall, F1-score, MAE, MSE).
- Provides a clear training, validation, and testing pipeline.
- Saves the trained model for future inference.

## Software and Hardware Requirements:

### Software Requirements:
- Python 3.10+
- PyTorch (Deep Learning Framework)
- `timm` library for pretrained ConvNeXt architecture
- Albumentations for data augmentation
- Jupyter Notebook for model training and evaluation

### Hardware Requirements:
- System with at least 4GB RAM
- GPU (CUDA-enabled) preferred for faster training and inference

## Dataset:
- **Name**: UTKFace Dataset  
- **Link**: [UTKFace Dataset on Kaggle](https://www.kaggle.com/datasets/jangedoo/utkface-new)  
- **Description**: Dataset contains over 20,000 face images of individuals aged 1 to 116 years. Each image filename includes age, gender, and ethnicity.  

### Preprocessing:
- Removed images with invalid ages (kept ages 1–119).
- Converted images to tensors and normalized pixel values.

### Dataset Split:
- Training: 72.25%  
- Validation: 12.75%  
- Testing: 15%  

## Technologies Used:
- **Model Architecture**: ConvNeXt-Base (from `timm`)
- **Framework**: PyTorch
- **Data Augmentation**: Albumentations
- **Evaluation**: scikit-learn for metrics and visualization

## Methodology:
1. **Input**: Load facial images from the UTKFace dataset.
2. **Preprocessing**: Apply augmentations and normalization.
3. **Model**: Fine-tune a pretrained ConvNeXt-Base CNN on the dataset.
4. **Output**: Predict the age for each image and evaluate performance using metrics.

## Data Preprocessing:
- **Training Augmentation**:
  - Resize: 256×256 → Random Crop: 224×224
  - Horizontal Flip
  - Random Brightness/Contrast
  - Coarse Dropout
  - Normalize (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
- **Validation & Test**:
  - Resize: 224×224
  - Normalize using ImageNet stats

## Training Details:
- **Epochs**: 25
- **Batch Size**: 32
- **Loss Function**: Mean Squared Error (MSE)
- **Optimizer**: Adam
- **Learning Rate Scheduler**: ReduceLROnPlateau
- **Mixed Precision**: Enabled using `torch.cuda.amp` for faster computation
- **Best Model Saving**: Based on lowest validation loss

## Evaluation:
- **Final Accuracy**: 70.85%
- **Metrics**:
  - Confusion Matrix
  - Classification Report (Precision, Recall, F1-score)
- **Error Metrics**:
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)

## System Architecture:
- **Model**: ConvNeXt-Base pretrained on ImageNet and fine-tuned on UTKFace
- **Workflow**: Dataset → Preprocessing → Training → Evaluation → Saving Model

## Project Structure:
Task-1-Age-Detection/  
├── age_detection_model.ipynb  
├── requirements.txt  
├── saved_model/  
│   └── age_model.pth  
├── README.md

## Model Weights
Download the trained model weights from Google Drive:

[Download Model Weights](https://drive.google.com/drive/folders/1TicMGVhmYdz6eaIqyPhmUM5a0gE1SKYt?usp=sharing)

## Setup Instructions
1. Clone this Repository:
```bash
git clone <https://github.com/manojrd21/Internship-Tasks.git>
cd Task-1-Age-Detection
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Open the Jupyter notebook:
```bash
jupyter notebook age_detection_model.ipynb
```
4. Run the notebook to:
- Load and preprocess the dataset
- Train the model
- Evaluate performance metrics
- Save the model

## Requirements
The full list of dependencies is in requirements.txt. Key libraries:
- torch
- torchvision
- timm
- albumentations
- scikit-learn
- numpy
- matplotlib
- pandas

## Output
- Model accuracy and evaluation metrics (precision, recall, confusion matrix) are displayed at the end of the notebook.
- Graphs for training and validation loss are plotted.
- The saved model is stored in the saved_model/ directory.

## Limitations:
- No GUI implemented (not required for this task).
- Accuracy may vary based on image quality and age distribution in the dataset.

## Future Scope:
- Build a web-based GUI for real-time age prediction.
- Extend the model to predict multiple attributes (gender, ethnicity).
- Deploy the model to cloud platforms for large-scale usage.

## Conclusion:
This project demonstrates a robust CNN-based approach for age prediction from facial images. By fine-tuning a pretrained ConvNeXt model, the system achieves over 70% accuracy and provides a solid baseline for further improvements.

## Author:
Manoj Dhanawade
NULLCLASS Internship Task