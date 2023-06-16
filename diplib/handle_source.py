import cv2
import numpy as np

def get_gray_image(filename: str) -> np.ndarray:
    address = filename
    image = cv2.imread(address, cv2.IMREAD_GRAYSCALE)
    return image

def get_color_image_rgb(filename: str) -> np.ndarray:
    address = filename
    image = cv2.imread(address, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_color_image_hsi(filename: str) -> np.ndarray:
    address = filename
    image = cv2.imread(address, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return image

def get_video_frames(filename: str) -> np.ndarray:
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

def export_video(
        filename: str,
        frames: np.ndarray,
        codec='avc1',
        fps=22) -> None:
    frame_len, frame_height, frame_width, _ = frames.shape
    fourcc = cv2.VideoWriter_fourcc(*codec)
    out = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

    for idx,frame in enumerate(frames, 1):
        out.write(frame)
        print(f'{100 * idx / frame_len:>4.2f}% ({idx:>4d}/{frame_len:>4d}) frames processing...', end='\r')
    out.release()