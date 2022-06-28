import cv2
import os

root_dir = os.path.dirname(__file__)
emoji_directory = os.path.join(root_dir, "modules/anti_spoofing/challenge/emoji")

# _________________________ hand config ______________________________ #

hand = {
    "rectangle_color": (200, 0, 200),
    "rectangle_thickness": 2,
    "font": cv2.FONT_HERSHEY_PLAIN,
    "font_scale": 2,
    "font_color": (200, 0, 200),
    "font_thickness": 2
}

gesture = {
    "logging": os.path.join(root_dir, "modules/gesture", "key_points.csv"),
    "model_location": os.path.join(root_dir, "modules/gesture/key_points_classifier.tflite"),
    "gestures_label": os.path.join(root_dir, "modules/gesture/key_points_label.csv")
}

face = {
    "nose_tip" : 1,
    "corner_right_lip": 61,
    "corner_left_lip": 291,
    "corner_right_eye": 33,
    "corner_left_eye": 263,
    "chin": 199,
    "special_points_join": [1, 61, 291, 33, 263, 199]
}

head_pose = {
    1: "You are looking left",
    2: "You are looking right",
    3: "You are looking down",
    4: "You are looking up",
    5: "You are looking forward",
}

challenge = {
    'time_per_question': 10,
    'consecutive': 50
}