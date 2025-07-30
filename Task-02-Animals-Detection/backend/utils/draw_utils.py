import cv2

def draw_boxes(image, boxes, class_names, carnivores=[]):
    # Return original image if no detections
    if boxes is None or len(boxes) == 0:
        return image

    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = f"{class_names[cls_id]} {conf:.2f}"

        # Red for carnivores, green otherwise
        color = (0, 0, 255) if class_names[cls_id] in carnivores else (0, 255, 0)
        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness=4)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1.5
        thickness = 3
        padding = 10

        (text_width, text_height), baseline = cv2.getTextSize(label, font, font_scale, thickness)

        text_x = x1
        text_y = y1 - 10 if y1 - 10 > text_height + padding else y1 + text_height + padding

        cv2.rectangle(
            image,
            (text_x - padding, text_y - text_height - padding),
            (text_x + text_width + padding, text_y + baseline + padding),
            (0, 0, 0),
            thickness=cv2.FILLED
        )

        cv2.putText(
            image,
            label,
            (text_x, text_y),
            font,
            font_scale,
            (255, 255, 255),
            thickness
        )

    return image
