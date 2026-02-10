"""
Test camera indeces 1-10 and report those found by OpenCV.
"""
import cv2

found = []
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print()
        print("#######################################")
        print(f">>> Camera device found for index {i}")
        print("#######################################")
        print()
        found.append(i)
    cap.release()

print()
print("Camera device indeces found:")
print(", ".join(map(str, found)))