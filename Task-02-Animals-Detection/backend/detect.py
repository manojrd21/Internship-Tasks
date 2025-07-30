import os
import cv2
import numpy as np
from ultralytics import YOLO
import importlib.util

# Load Paths
MODEL_PATH = "C:/Users/ADMIN/Desktop/Tasks/Task-2-Animals-Detection/saved_model/best.pt"
OUTPUT_IMAGES_DIR = "C:/Users/ADMIN/Desktop/Tasks/Task-2-Animals-Detection/backend/outputs/detected_images"
OUTPUT_VIDEOS_DIR = "C:/Users/ADMIN/Desktop/Tasks/Task-2-Animals-Detection/backend/outputs/detected_videos"
CLASS_MAPPING_PATH = "C:/Users/ADMIN/Desktop/Tasks/Task-2-Animals-Detection/backend/utils/class_mapping.py"
DRAW_UTILS_PATH = "C:/Users/ADMIN/Desktop/Tasks/Task-2-Animals-Detection/backend/utils/draw_utils.py"

# Import utility modules
def import_module_from_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class_mapping = import_module_from_path("class_mapping", CLASS_MAPPING_PATH)
draw_utils = import_module_from_path("draw_utils", DRAW_UTILS_PATH)
CLASS_NAMES = class_mapping.CLASS_NAMES
CARNIVORES = class_mapping.CARNIVORES
draw_boxes = draw_utils.draw_boxes

# Load model
model = YOLO(MODEL_PATH)
CONFIDENCE_THRESHOLD = 0.5

# Ensure output folders exist
os.makedirs(OUTPUT_IMAGES_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)

def iou(box1, box2):
    xA = max(box1[0], box2[0])
    yA = max(box1[1], box2[1])
    xB = min(box1[2], box2[2])
    yB = min(box1[3], box2[3])
    interArea = max(0, xB - xA) * max(0, yB - yA)
    box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    return interArea / float(box1Area + box2Area - interArea + 1e-6)

def is_new_instance(new_box, existing_boxes, iou_threshold=0.5):
    for prev_box in existing_boxes:
        if iou(new_box, prev_box) >= iou_threshold:
            return False
    return True

def detect(file_path):
    try:
        print(f"[INFO] Detect called with file_path: {file_path}")

        if not os.path.exists(file_path):
            return {"error": "File not found."}

        file_ext = os.path.splitext(file_path)[-1].lower()
        is_image = file_ext in [".jpg", ".jpeg", ".png"]
        is_video = file_ext in [".mp4", ".avi", ".mov", ".mkv"]

        carnivore_total_count = 0

        if is_image:
            print("[INFO] Processing as image")
            image = cv2.imread(file_path)
            if image is None:
                return {"error": "Failed to load image."}

            results = model(image)[0]
            boxes = [box for box in results.boxes if float(box.conf[0]) >= CONFIDENCE_THRESHOLD]
            classes = model.names

            carnivore_total_count = sum(
                1 for box in boxes if classes[int(box.cls[0])] in CARNIVORES
            )

            annotated = draw_boxes(image, boxes, classes, carnivores=CARNIVORES)
            filename = os.path.basename(file_path)
            output_filename = f"detected_{filename}"
            out_path = os.path.join(OUTPUT_IMAGES_DIR, output_filename)
            cv2.imwrite(out_path, annotated)

            print(f"[INFO] Image detection completed. Output: {out_path}")

            return {
                "output_path": output_filename,  # return only the filename
                "carnivores_detected": carnivore_total_count,
                "type": "image"
            }

        elif is_video:
            print("[INFO] Processing as video")
            cap = cv2.VideoCapture(file_path)
            if not cap.isOpened():
                return {"error": "Failed to open video."}

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)

            filename = os.path.basename(file_path).rsplit(".", 1)[0] + ".webm"
            output_filename = f"detected_{filename}"
            out_path = os.path.join(OUTPUT_VIDEOS_DIR, output_filename)
            writer = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*"VP80"), fps, (width, height))

            seen_boxes = []

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                results = model(frame)[0]
                boxes = [box for box in results.boxes if float(box.conf[0]) >= CONFIDENCE_THRESHOLD]
                classes = model.names

                for box in boxes:
                    class_id = int(box.cls[0])
                    class_name = classes[class_id]

                    if class_name in CARNIVORES:
                        x1, y1, x2, y2 = box.xyxy[0].tolist()
                        current_box = [x1, y1, x2, y2]

                        if is_new_instance(current_box, seen_boxes):
                            seen_boxes.append(current_box)
                            carnivore_total_count += 1

                annotated = draw_boxes(frame, boxes, classes, carnivores=CARNIVORES)
                writer.write(annotated)

            cap.release()
            writer.release()

            print(f"[INFO] Video detection completed. Output: {out_path}")

            return {
                "output_path": output_filename,  # return only the filename
                "carnivores_detected": carnivore_total_count,
                "type": "video"
            }

        else:
            return {"error": "Unsupported file type. Upload image or video."}

    except Exception as e:
        print("[EXCEPTION] Error in detect():", str(e))
        return {"error": str(e)}
