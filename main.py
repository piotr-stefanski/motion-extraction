from PIL import Image, ImageChops
import cv2
import numpy as np


def read_video():
    cap = cv2.VideoCapture('data/motion.mp4')
    back_n_frames = 5
    i = 0
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_pil = Image.fromarray(frame)

        inverted_frame = ImageChops.invert(frame_pil.convert('RGB'))
        inverted_frame.putalpha(128)

        print(len(frames), back_n_frames, len(frames) >= back_n_frames)
        if len(frames) >= back_n_frames:
            prev_frame = frames[i-back_n_frames]

            prev_frame.paste(inverted_frame, (0, 0), mask=inverted_frame)
            frame = np.asarray(prev_frame)

        i += 1
        frames.append(frame_pil)
        cv2.imshow('img', frame)
        cv2.waitKey(0)


read_video()
