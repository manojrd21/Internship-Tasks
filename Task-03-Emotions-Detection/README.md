# Project Title: Emotion Detection through Voice (Female Only)

## Objective:
To develop a voice-based emotion detection system that first identifies the speaker's gender. If the gender is female, the system proceeds to detect emotion; otherwise, it prompts the user to upload a female voice.

## Problem Statement:
In many emotion detection systems, gender differentiation is not taken into account. Male and female voices have different acoustic properties, which can lead to inaccurate emotion predictions. This system filters for female voices before emotion classification to ensure better performance.

## Scope of the Project:
- Accepts audio input via file upload or browser-based recording
- Detects gender from the audio
- If gender is female: proceeds to emotion detection
- If gender is male: prompts the user to upload a female voice
- Displays result using a popup message box

## Software and Hardware Requirements:

### Software Requirements:
- Python 3.10
- Flask
- TensorFlow 2.18.0
- Librosa
- HTML, CSS, JavaScript

### Hardware Requirements:
- System with at least 4GB RAM
- Microphone (for audio recording)
- Modern browser (Chrome, Edge, Firefox)

## Dataset
- **For Gender Detection**: Gender Recognition by Voice(original)
- **Link**: [Download Dataset](https://www.kaggle.com/datasets/murtadhanajim/gender-recognition-by-voiceoriginal)

- **For Emotions Detection**: RAVDESS Emotional speech audio
- **Link**: [Download Dataset](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)

## Technologies Used:
- Deep Learning (CNN, CRNN)
- Flask (Backend Framework)
- HTML5, CSS3, JavaScript (Frontend)
- Librosa (Audio Processing)

## Methodology:
1. **Audio Input:** User either uploads an audio file or records voice through the browser.
2. **Gender Detection:**
   - Trained CNN model detects gender from the input.
   - If male: prompt shown – "Please upload female voice."
   - If female: proceeds to emotion detection.
3. **Emotion Detection:**
   - Trained CRNN model classifies emotions such as Happy, Sad, Angry, Neutral, etc.
4. **Output:** Detected emotion is shown in a popup message box.

## System Architecture:
- **Frontend:** `index.html`, `style.css`, `recorder.js`
- **Backend:** `Flask (app.py)`
- **Models:** Trained models saved as `.h5` files
- **Utils:** Preprocessing and prediction logic in `utils.py`

## Project Structure
```bash
Task-3-Emotions-Detection/
├─ backend/
│  ├─ __init__.py
│  ├─ app.py
│  └─ utils.py
├─ frontend/
│  ├─ templates/
│  │  └─ index.html
│  └─ static/
│     ├─ recorder.js
│     └─ style.css
├─ saved_models/
│  ├─ gender_model.keras
│  └─ emotions_model.keras
├─ uploads/
│  └─ (created automatically if missing)
├─ venv/
├─ testing_audios
├─ emotions_detection_model.ipynb
├─ gender_detection_model.ipynb
├─ requirements.txt
└─ README.md
```

## Model Weights
Download the trained model weights from the link below:

[Download Gender_Model Weights](https://drive.google.com/drive/folders/1D3fZTC-KEMrb4Og2kmbTdig7auK9WiMZ?usp=sharing)

[Download Emotions_Model Weights](https://drive.google.com/drive/folders/1D3fZTC-KEMrb4Og2kmbTdig7auK9WiMZ?usp=sharing)

## Steps to Run the Project:

1. Clone the repository:
```bash
git clone <https://github.com/manojrd21/Internship-Tasks.git>
cd Task-3-Emotions-Detection
```

2. Create a virtual environment:
```bash
py -3.10 -m venv venv
source venv/bin/activate # On Windows
```

3. Install Dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask application:
```bash
python -m backend.app
```

5. Open the browser and visit:
```bash
http://127.0.0.1:5000
```

## Requirements
The list of dependencies is in requirements.txt. Key libraries:
- Flask==3.0.3
- numpy==1.26.4
- librosa==0.10.1
- tensorflow==2.18.0
- soundfile==0.12.1
- Werkzeug==3.0.1

## Output:
- If gender is **male**:
- Popup: "Please upload female voice"
- If gender is **female**:
- Popup: "Emotion: [detected_emotion]"

## Limitations:
- System only works for female voice emotion classification.
- Accuracy may vary based on background noise and voice quality.
- Does not support real-time streaming beyond browser-recorded audio.

## Future Scope:
- Expand the system to handle both male and female emotion detection separately.
- Integrate real-time speech-to-text and emotion tagging.
- Deploy the system on cloud platforms for broader accessibility.

## Conclusion:
This project demonstrates a robust and focused approach to gender-specific emotion detection using voice. By filtering gender before emotion classification, the system enhances the reliability of its predictions and creates a foundation for further enhancements in human-computer interaction.

## Author:
Manoj Dhanawade  
NULLCLASS Internship Task
