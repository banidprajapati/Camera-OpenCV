import cv2
import os
import time

video_writer = None  # Initialize video_writer outside the function
filename = None # Initialize filename outside the function

def start_recording(cam):
    global video_writer, filename
    # Start recording video and return the VideoWriter object and filename
    output_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "Output/Videos")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    vid_time = time.strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"VID_{vid_time}.mp4")

    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cam.get(cv2.CAP_PROP_FPS)) or 30

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

    print(f"Recording started: {filename}")

def end_recording(cam):
    global video_writer, filename # Access the global variable
    # Release the VideoWriter object
    if video_writer is not None:
        video_writer.release()
        video_writer = None
        print("Recording ended.")
    else:
        print("No recording in progress.")