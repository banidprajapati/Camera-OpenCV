from utils import utils_camera
from utils import utils_video
import cv2
import tkinter as tk
from utils.utils_control import create_controls

flip_state = [True]
face_detection_enabled = [False]  # Use list for mutability
alpha = [1.0] # Use list for mutability (contrast)
beta = [0]    # Use list for mutability (brightness)

# --- Face detection code here ---
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return frame

def set_brightness(val):
    beta[0] = int(val)

def set_contrast(val):
    alpha[0] = float(val)

def toggle_face_detection():
    face_detection_enabled[0] = not face_detection_enabled[0]
    if face_detection_enabled[0]:
        face_detect_btn.config(text="Face Detection: ON")
    else:
        face_detect_btn.config(text="Face Detection: OFF")

def update():
    ret, frame = cam.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        root.quit()
        return

    # Flip the frame horizontally if flip_state[0] is True
    if flip_state[0]:
        frame = cv2.flip(frame, 1)

    # Apply brightness and contrast
    frame = cv2.convertScaleAbs(frame, alpha=alpha[0], beta=beta[0])

    # Run face detection if enabled
    if face_detection_enabled[0]:
        frame = detect_faces(frame)

    # Check if frame is valid before processing
    if frame is not None:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        _, buf = cv2.imencode('.png', cv2.cvtColor(rgb_frame, cv2.COLOR_BGR2RGBA))
        img_bytes = buf.tobytes()
        imgtk = tk.PhotoImage(data=img_bytes)
        
        label.imgtk = imgtk
        label.configure(image=imgtk)

    # Record video if recording is active
    if utils_video.video_writer is not None:
        utils_video.video_writer.write(frame)

    root.after(5, update)

root = tk.Tk()
root.title("Vertex Cam")

label = tk.Label(root)
label.pack()

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    sys.exit()

# ------ Buttons ------
btn_frame = tk.Frame(root)
btn_frame.pack()

controls = create_controls(
    btn_frame,
    lambda: utils_camera.flip_camera(cam, flip_state),
    lambda: utils_camera.capture_camera(cam, flip_state),
    lambda: utils_video.start_recording(cam),
    lambda: utils_video.end_recording(cam),
    toggle_face_detection,
    set_brightness,
    set_contrast,
    alpha,
    beta
)

root.after(0, update)
root.mainloop()

cam.release()
cv2.destroyAllWindows()