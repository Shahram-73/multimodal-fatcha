import cv2
import config
from modules.hand_landmarks import HandLandmark
from modules.face_detection import FaceDetection
from modules.gesture.keypoint_classifier import KeyPointClassifier
from modules.gesture.key_points_logging import CSVLogging
from modules.voice_assistant import VoiceAssistant
from modules.eye_blinking.eye_status import *


import csv

cap = cv2.VideoCapture(0)  # To use a video file as input: cv2.VideoCapture('filename.mp4')
cap.set(3, config.camera['width'])
cap.set(4, config.camera['height'])

face_detection = FaceDetection()
hand_landmarks = HandLandmark()
voice_assistant = VoiceAssistant()

key_points_classifier = KeyPointClassifier()
with open(config.gesture['gestures_label'], encoding='utf-8-sig') as f:
    keypoint_classifier_labels = csv.reader(f)
    keypoint_classifier_labels = [
        row[0] for row in keypoint_classifier_labels
    ]
voice_assistant.welcome()
mode = int(input("What is your mode:  "))
if mode=='2':
    while cap.isOpened():
        # Read the frame
        success, frame = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        face_detected_frame = face_detection.detect(cv2.flip(frame, 1))
        hand_face_detected_frame, results = hand_landmarks.detect(face_detected_frame, True, landmarks=True)


        if results.multi_hand_landmarks is not None:
            for h_landmarks in results.multi_hand_landmarks:
                class_id = key_points_classifier(
                    CSVLogging.pre_process_landmark(
                        CSVLogging.landmark_list(hand_face_detected_frame, h_landmarks)
                    )
                )
                cv2.putText(
                    hand_face_detected_frame,
                    "Finger Gesture:" + keypoint_classifier_labels[class_id],
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0),
                    4,
                    cv2.LINE_AA
                )


        cv2.imshow('img', hand_face_detected_frame)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    # Release the VideoCapture object
    cap.release()

elif mode == 1:
    voice_assistant.getcommand()
    while cap.isOpened():
        # Read the frame
        success, frame = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        face_detected_frame = face_detection.detect(cv2.flip(frame, 1))
        hand_face_detected_frame, results = hand_landmarks.detect(face_detected_frame, True, landmarks=True)

        if results.multi_hand_landmarks is not None:
            for h_landmarks in results.multi_hand_landmarks:
                class_id = key_points_classifier(
                    CSVLogging.pre_process_landmark(
                        CSVLogging.landmark_list(hand_face_detected_frame, h_landmarks)
                    )
                )
                cv2.putText(
                    hand_face_detected_frame,
                    "Finger Gesture:" + keypoint_classifier_labels[class_id],
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0),
                    4,
                    cv2.LINE_AA
                )
                if class_id == 5 :
                    print ("access accepted")
                else:
                    print("access denied")
        cv2.imshow('img', hand_face_detected_frame)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    # Release the VideoCapture object
    cap.release()