"""
Run this file using `streamlit run path/to/this/file.py path/to/model.pt -- --webcam <webcam_idx>`
"""
from pathlib import Path
import cv2
import streamlit as st
from ultralytics import YOLO
import argparse


class CameraYoloInferenceApp:
    """
    A class to perform object detection inference with YOLO.
    """
    def __init__(self, model_path, webcam_idx: int = 0):
        """Initialize the Inference class."""
        self.conf = 0.25  # Confidence threshold for detection
        self.iou = 0.45  # Intersection-over-Union (IoU)
        self.ann_frame = None  # Container for the annotated frame display
        self.selected_ind = []  # Selected class indices for detection
        self.webcam_idx = webcam_idx
        self.model = YOLO(model_path)

    def inference(self):
        """Perform real-time object detection inference on video or webcam feed."""
        st.set_page_config(page_title="Streamlit App", layout="wide")
        st.title("Object Detection with YOLO")

        with st.sidebar:
            st.image("https://imaging.epfl.ch/resources/logo-for-gitlab.svg", width=250)

        st.sidebar.title("Configuration")
        self.conf = float(
            st.sidebar.slider("Confidence Threshold", 0.0, 1.0, self.conf, 0.01)
        )
        self.iou = float(st.sidebar.slider("IoU Threshold", 0.0, 1.0, self.iou, 0.01))
        self.ann_frame = st.container().empty()

        class_names = list(self.model.names.values())
        selected_classes = st.sidebar.multiselect("Classes", class_names, default=class_names[:3])
        self.selected_ind = [class_names.index(option) for option in selected_classes]
        if not isinstance(self.selected_ind, list):
            self.selected_ind = list(self.selected_ind)

        if st.sidebar.button("Start Camera", use_container_width=True):
            stop_button = st.button("Stop Camera", use_container_width=True)

            cap = cv2.VideoCapture(self.webcam_idx)
            if not cap.isOpened():
                st.error(f"Could not open camera with ({self.webcam_idx=}).")
                return

            while cap.isOpened():
                success, frame = cap.read()
                if not success:
                    st.warning(
                        "Failed to read frame from camera. Is it connected properly?"
                    )
                    break

                results = self.model(
                    frame, conf=self.conf, iou=self.iou, classes=self.selected_ind
                )

                annotated_frame = results[0].plot()  # Add annotations on frame

                if stop_button:
                    cap.release()
                    st.stop()

                self.ann_frame.image(
                    annotated_frame,
                    channels="BGR",
                    use_container_width=True,
                )

            cap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run YOLO inference in a Streamlit web app.")
    parser.add_argument("model", help="Path to the YOLO model file.")
    parser.add_argument("--webcam", type=int, default=0, help="Webcam index (default: 0).")
    args = parser.parse_args()

    model_path = args.model
    webcam_idx = args.webcam

    assert Path(
        model_path
    ).exists(), f"Could not find this model file: {Path(model_path).resolve()}"

    CameraYoloInferenceApp(model_path=model_path, webcam_idx=webcam_idx).inference()
