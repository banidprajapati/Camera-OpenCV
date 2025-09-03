import cv2
import os
import time


def flip_camera(cam, flip_state):
    flip_state[0] = not flip_state[0]

def capture_camera(cam, flip_state):
    # Capture the current frame and save as capture.jpg
    _, frame = cam.read()
    
    if flip_state[0]:
        frame = cv2.flip(frame, 1)
    
    output_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "Output/Images")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    img_time = time.strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"IMG_{img_time}.jpg")
    cv2.imwrite(filename, frame)
    print(f"Image saved as {filename}")
