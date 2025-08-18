import tkinter as tk
import cv2 as cv
import sys

root = tk.Tk()
root.title("Camera Feed")

label = tk.Label(root)
label.pack()

cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    sys.exit()

def update():
    ret, frame = cam.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        root.quit()
        return

    flipped = cv.flip(frame, 1)
    rgb_frame = cv.cvtColor(flipped, cv.COLOR_BGR2RGB)
    # Encode as PNG to get bytes for Tkinter PhotoImage
    _, buf = cv.imencode('.png', cv.cvtColor(flipped, cv.COLOR_BGR2RGBA))
    img_bytes = buf.tobytes()
    imgtk = tk.PhotoImage(data=img_bytes)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    root.after(10, update)

root.after(0, update)

btn_quit = tk.Button(root, text="Quit", command=root.quit)
btn_quit.pack()

root.mainloop()

cam.release()
cv.destroyAllWindows()
