from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os
import uuid
from detect import detect

app = Flask(
    __name__,
    template_folder="C:/Users/ADMIN/Desktop/Tasks/Task-2-Animals-Detection/frontend/templates",
    static_folder="C:/Users/ADMIN/Desktop/Tasks/Task-2-Animals-Detection/frontend/static"
)
CORS(app)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def handle_detection():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        ext = os.path.splitext(file.filename)[-1]
        unique_filename = f"{uuid.uuid4().hex}{ext}"
        saved_path = os.path.join(UPLOAD_DIR, unique_filename)
        file.save(saved_path)

        result = detect(saved_path)

        if "error" in result:
            return jsonify(result), 500

        # Extract only the filename to send to the frontend
        output_filename = os.path.basename(result["output_path"])

        return jsonify({
            "output_filename": output_filename,
            "carnivores_detected": result["carnivores_detected"],
            "type": result["type"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_output/<path:filename>")
def get_output_file(filename):
    base_dirs = [
        "C:/Users/ADMIN/Desktop/Tasks/Task-2-Animals-Detection/backend/outputs/detected_images",
        "C:/Users/ADMIN/Desktop/Tasks/Task-2-Animals-Detection/backend/outputs/detected_videos"
    ]
    for base in base_dirs:
        full_path = os.path.join(base, filename)
        if os.path.exists(full_path):
            if filename.lower().endswith(".webm"):
                return send_from_directory(base, filename, mimetype="video/webm")
            return send_from_directory(base, filename)
    return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
