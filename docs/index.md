# Object Detection with YOLO

In this workshop, we'll go through the steps of acquiring images, annotating them, training an object detection model, and testing it in real time on USB microscopes.

```{mermaid}
flowchart LR
    A(🔬 Acquisition) --> B(🖌️ Annotation)
    B --> C(🎓 Training)
    C --> D(⚖️ Validation)
    D --> E(🔋 Inference)
```

![Introduction](./assets/intro.gif)

We will implement a system based on a [YOLO](https://en.wikipedia.org/wiki/You_Only_Look_Once) model, which is a state-of-the-art method for real-time object detection. YOLO models usually offer good performance and require few images for training, making them particularly useful for applications in computer vision and scientific image analysis.

```{dropdown} How does YOLO work?

The original YOLO model was designed in 2015 ([Redmon et al, 2015](https://doi.org/10.48550/arXiv.1506.02640)); it was a convolutional Neural Network (CNN) that predicted and classified bounding boxes in a single forward pass (hence the name - *You Only Look Once*), enabling fast, real-time predictions.

![Yolo schematic](./assets/yolo-2015.png)

Since then, more modern versions of the model have been developed (YOLOv2, YOLOv3...), introducing architectural changes and improvements to make the model faster, more accurate, and more versatile ([Models](https://docs.ultralytics.com/models/#featured-models)).
```

In this workshop, we will train a YOLO model to automatically recognize different kinds of seeds and spices from our kitchen, using a USB microscope as a camera device.

## Microscope Setup

To complete this workshop, you will need:

- 🔬 A USB microscope (connected via USB-A)
- 🫘 Some seeds to capture images of (e.g., quinoa, chia)
- 🐍 Python installed on your system

![Camera Setup](./assets/camera_setup.png)

### Test the microscope

Once plugged in, you should also be able to start the microscope camera and capture images.

`````{tab-set}
````{tab-item} Windows
Open the `Camera` app from the start menu. In the *Settings*, you should be able to select the USB microscope as an input device instead of your webcam.
````
````{tab-item} Mac
Open the `Photo Booth` app from the Applications folder. In the *Settings*, you should be able to select the USB microscope as an input device instead of your webcam.
````
````{tab-item} Linux
1. Install [Cheese](https://en.wikipedia.org/wiki/Cheese_(software)) using `sudo apt install cheese`.
2. Launch it from the terminal with the `cheese` command.
3. In the *Preferences*, you should be able to select the USB microscope as a device instead of your webcam.
````
`````

Now that you're set up, let's dive in - starting with acquiring some training images.