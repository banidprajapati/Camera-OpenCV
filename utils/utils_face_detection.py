import cv2

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect_faces(image):
    """
    Detects faces in an image using Haar cascades.

    Args:
        image (numpy.ndarray): Input image (BGR format).

    Returns:
        List of rectangles (x, y, w, h) for each detected face.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return faces