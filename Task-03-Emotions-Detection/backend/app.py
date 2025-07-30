from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from backend.utils import predict_gender_then_emotion
from pathlib import Path

# Point Flask to the frontend templates/static
BASE_DIR = Path(__file__).parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"
app = Flask(
    __name__,
    template_folder=str(FRONTEND_DIR / "templates"),
    static_folder=str(FRONTEND_DIR / "static")
)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'wav'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request."})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file."})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        result = predict_gender_then_emotion(file_path)
        return jsonify(result)

    return jsonify({"error": "Invalid file format. Only WAV allowed."})

if __name__ == '__main__':
    app.run(debug=True)
