from ultralytics import YOLO
import cv2
import cvzone
import math
import time
from datetime import datetime
import os

cap = cv2.VideoCapture(0)  # For Video

model = YOLO("best.pt")

classNames = ["Smoking", "Weapon"]

prev_frame_time = 0
new_frame_time = 0

# Specify the directory path where you want to save the photos
photo_directory = "F:\DETECTED PERSON"

# Ensure the directory exists, create it if necessary
os.makedirs(photo_directory, exist_ok=True)

while True:
    new_frame_time = time.time()
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            class_name = classNames[cls]

            cvzone.putTextRect(img, f'{class_name} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

            # Check if the detected object is smoking or a weapon
            if class_name in ["Smoking", "Weapon"]:
                # Capture photo
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                photo_name = f"{class_name}_{timestamp}.jpg"
                photo_path = os.path.join(photo_directory, photo_name)
                cv2.imwrite(photo_path, img)
                print(f"Photo captured: {photo_path}")

    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
