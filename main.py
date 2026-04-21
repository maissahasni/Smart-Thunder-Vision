import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision
import numpy as np
import random
import threading
import urllib.request
import os
from playsound import playsound

# Play sound without freezing
def play_thunder():
    threading.Thread(target=playsound, args=("thunder.mp3",), daemon=True).start()

# Download hand landmarker model if not present
MODEL_PATH = "hand_landmarker.task"
if not os.path.exists(MODEL_PATH):
    print("Downloading hand landmarker model...")
    urllib.request.urlretrieve(
        "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task",
        MODEL_PATH
    )
    print("Done.")

# Mediapipe setup (new Tasks API)
base_options = mp_python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2
)
detector = vision.HandLandmarker.create_from_options(options)

# Hand connections for drawing
HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

def draw_landmarks(img, landmarks):
    h, w = img.shape[:2]
    pts = [(int(lm.x * w), int(lm.y * h)) for lm in landmarks]
    for a, b in HAND_CONNECTIONS:
        cv2.line(img, pts[a], pts[b], (0, 255, 0), 2)
    for pt in pts:
        cv2.circle(img, pt, 4, (0, 0, 255), -1)

# Camera
cap = cv2.VideoCapture(0)

# Load images
background = cv2.imread("thunder.jpg")
background = cv2.resize(background,(900,600))

lightning = cv2.imread("lightning.png", cv2.IMREAD_UNCHANGED)
lightning = cv2.resize(lightning,(200,400))


# Finger counting function
# label: "Left" or "Right" as reported by mediapipe (mirrored in front-facing camera)
def count_fingers(hand_landmarks, label):
    fingers = []
    tipIds = [4, 8, 12, 16, 20]

    # Thumb: direction flips depending on hand side
    # Front-facing camera is mirrored, so "Right" label = hand on left of screen
    tip_x   = hand_landmarks[tipIds[0]].x
    knuckle_x = hand_landmarks[tipIds[0] - 1].x
    if label == "Right":
        fingers.append(1 if tip_x > knuckle_x else 0)
    else:
        fingers.append(1 if tip_x < knuckle_x else 0)

    # Other 4 fingers: tip y above pip y = finger up
    for i in range(1, 5):
        tip_y = hand_landmarks[tipIds[i]].y
        pip_y = hand_landmarks[tipIds[i] - 2].y
        fingers.append(1 if tip_y < pip_y else 0)

    return fingers.count(1)


# Overlay lightning (fast, bounds-safe, alpha-blended)
def overlay_lightning(bg, lightning, x, y):
    bh, bw = bg.shape[:2]
    lh, lw = lightning.shape[:2]

    # Clip to background bounds
    x1, y1 = max(x, 0), max(y, 0)
    x2, y2 = min(x + lw, bw), min(y + lh, bh)
    if x2 <= x1 or y2 <= y1:
        return bg

    lx1, ly1 = x1 - x, y1 - y
    lx2, ly2 = lx1 + (x2 - x1), ly1 + (y2 - y1)

    alpha = lightning[ly1:ly2, lx1:lx2, 3:4] / 255.0
    fg = lightning[ly1:ly2, lx1:lx2, :3].astype(np.float32)
    bg_region = bg[y1:y2, x1:x2].astype(np.float32)
    bg[y1:y2, x1:x2] = np.clip(fg * alpha + bg_region * (1 - alpha), 0, 255).astype(np.uint8)
    return bg


while True:

    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)
    detection_result = detector.detect(mp_image)

    screen = background.copy()
    finger_count = 0

    if detection_result.hand_landmarks:
        for i, hand_landmarks in enumerate(detection_result.hand_landmarks):
            label = detection_result.handedness[i][0].category_name  # "Left" or "Right"
            finger_count = max(finger_count, count_fingers(hand_landmarks, label))

            # Draw landmarks on camera feed
            draw_landmarks(img, hand_landmarks)

    # Lightning logic

    if finger_count >= 1:
        screen = overlay_lightning(screen, lightning, 100, 50)

    if finger_count >= 2:
        screen = overlay_lightning(screen, lightning, 350, 50)

    if finger_count >= 3:
        screen = overlay_lightning(screen, lightning, 600, 50)

    if finger_count >= 4:
        screen = overlay_lightning(screen, lightning, 200, 100)

    if finger_count >= 5:
        screen = overlay_lightning(screen, lightning, 500, 100)

    # Flash effect
    if finger_count > 0:
        if random.randint(0,10) > 7:
            screen = np.clip(screen.astype(np.int32) + 60, 0, 255).astype(np.uint8)
            play_thunder()

    # Show camera small
    cam = cv2.resize(img,(250,180))
    screen[400:580, 620:870] = cam

    cv2.putText(screen, f"Fingers: {finger_count}",
    (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1,
    (255,255,255), 2)

    cv2.imshow("Smart Thunder Vision", screen)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()