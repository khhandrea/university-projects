import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_gray_image(filename):
    address = filename
    image = cv2.imread(address, cv2.IMREAD_GRAYSCALE)
    return image

def get_color_image_rgb(filename):
    address = filename
    image = cv2.imread(address, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_color_image_hsi(filename):
    address = filename
    image = cv2.imread(address, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return image

def get_video_frames(filename):
    address = filename
    capture = cv2.VideoCapture(address)
    frames = []
    while capture.isOpened():
        run, frame = capture.read()
        if not run:
            break
        img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        frames.append(img)
    capture.release()
    return np.array(frames, dtype='uint8')