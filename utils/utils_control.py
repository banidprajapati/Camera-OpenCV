import tkinter as tk

def create_controls(frame, flip_callback, capture_callback, start_recording_callback, end_recording_callback, toggle_face_callback, set_brightness, set_contrast, alpha, beta):
    # Brightness slider
    brightness_slider = tk.Scale(frame, from_=-100, to=100, orient=tk.HORIZONTAL, label="Brightness", command=set_brightness)
    brightness_slider.set(beta[0])
    brightness_slider.pack(side=tk.LEFT)

    # Contrast slider
    contrast_slider = tk.Scale(frame, from_=0.5, to=3.0, resolution=0.1, orient=tk.HORIZONTAL, label="Contrast", command=set_contrast)
    contrast_slider.set(alpha[0])
    contrast_slider.pack(side=tk.LEFT)

    flip_btn = tk.Button(frame, text="Flip", padx=10, pady=10, width=15, command=flip_callback)
    flip_btn.pack(side=tk.LEFT)

    capture_btn = tk.Button(frame, text="Capture", padx=10, pady=10, width=15, command=capture_callback)
    capture_btn.pack(side=tk.LEFT)

    start_recording = tk.Button(frame, text="🎥 Start Video", padx=10, pady=10, width=15, command=start_recording_callback)
    start_recording.pack(side=tk.LEFT)

    end_recording = tk.Button(frame, text="⏹ Stop Video", padx=10, pady=10, width=15, command=end_recording_callback)
    end_recording.pack(side=tk.LEFT)

    face_detect_btn = tk.Button(frame, text="Face Detection: OFF", padx=10, pady=10, width=15, command=toggle_face_callback)
    face_detect_btn.pack(side=tk.LEFT)

    return {
        "brightness_slider": brightness_slider,
        "contrast_slider": contrast_slider,
        "flip_btn": flip_btn,
        "capture_btn": capture_btn,
        "start_recording": start_recording,
        "end_recording": end_recording,
        "face_detect_btn": face_detect_btn
    }