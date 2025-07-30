import os
import numpy as np
import librosa
from tensorflow.keras.models import load_model

# ===== Constants =====
SR = 22050
DURATION = 2.5
SAMPLES_PER_TRACK = int(SR * DURATION)
N_MELS = 128
GENDER_LABELS = ["Female", "Male"]
EMOTION_LABELS = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

# Load Models
gender_model = load_model("C:/Users/ADMIN/Desktop/Tasks/Task-3-Emotions-Detection/saved_models/gender_model.keras")
emotion_model = load_model("C:/Users/ADMIN/Desktop/Tasks/Task-3-Emotions-Detection/saved_models/emotions_model.keras")

# Helper Functions
def load_audio_fixed(path, sr=SR):
    y, _ = librosa.load(path, sr=sr, mono=True)
    if len(y) < SAMPLES_PER_TRACK:
        y = np.pad(y, (0, SAMPLES_PER_TRACK - len(y)))
    else:
        y = y[:SAMPLES_PER_TRACK]
    return y

def melspec_db(y, sr=SR, n_mels=N_MELS):
    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)
    return librosa.power_to_db(mel, ref=np.max)

def zscore_norm(x, eps=1e-6):
    return (x - np.mean(x)) / (np.std(x) + eps)

def prepare_input_for_cnn(m):
    return np.expand_dims(np.expand_dims(m, -1), 0)

# Prediction Function
def predict_gender_then_emotion(audio_path):
    if not os.path.exists(audio_path):
        return {"error": "Audio file not found."}

    try:
        y = load_audio_fixed(audio_path)
        mel_db = melspec_db(y)

        # Predict gender
        gender_input = prepare_input_for_cnn(mel_db)
        g_probs = gender_model.predict(gender_input, verbose=0)[0]
        g_idx = int(np.argmax(g_probs))
        gender = GENDER_LABELS[g_idx]

        if gender == "Male":
            return {"gender": gender, "message": "Please upload a female voice."}

        # Predict emotion
        mel_db_norm = zscore_norm(mel_db)
        emotion_input = prepare_input_for_cnn(mel_db_norm)
        e_probs = emotion_model.predict(emotion_input, verbose=0)[0]
        e_idx = int(np.argmax(e_probs))
        emotion = EMOTION_LABELS[e_idx]

        return {
            "gender": gender,
            "emotion": emotion,
            "message": "Emotion detected successfully."
        }

    except Exception as e:
        return {"error": str(e)}
