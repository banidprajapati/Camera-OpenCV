import tkinter as tk
import cv2
import sys
import time
import os

flip_state = [True]

def flip_camera():
    flip_state[0] = not flip_state[0]
    
def capture_camera():
    # Capture the current frame and save as capture.jpg
    _, frame = cam.read()
    
    if flip_state[0]:
        frame = cv2.flip(frame, 1)
        
        output_dir = "Images/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        img_time = time.strftime("%Y%m%d_%H%M%S")
        filename = f"Images/IMG_{img_time}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    
def update():
    ret, frame = cam.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        root.quit()
        return

    # Flip the frame horizontally if flip_state[0] is True
    if flip_state[0]:
        frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Encode as PNG to get bytes for Tkinter PhotoImage
    _, buf = cv2.imencode('.png', cv2.cvtColor(rgb_frame, cv2.COLOR_BGR2RGBA))
    

        
    img_bytes = buf.tobytes()
    imgtk = tk.PhotoImage(data=img_bytes)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    root.after(5, update)

root = tk.Tk()
root.title("Vertex Cam")

label = tk.Label(root)
label.pack()

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    sys.exit()

# Frame to hold buttons side by side
btn_frame = tk.Frame(root)
btn_frame.pack()

# Button to flip camera
flip_btn = tk.Button(btn_frame, text="Flip", padx=10, pady=10, width=15, command=flip_camera)
flip_btn.pack(side=tk.LEFT)

# Button to capture camera
capture_btn = tk.Button(btn_frame, text="Capture", padx=10, pady=10, width=15, command=capture_camera)
capture_btn.pack(side=tk.LEFT)

root.after(0, update)
root.mainloop()

cam.release()
cv2.destroyAllWindows()