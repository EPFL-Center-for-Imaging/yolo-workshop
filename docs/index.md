# Object Detection with Ultralytics YOLO

This workshop will introduce you to the fundamental concepts of object detection and guide you through the steps of acquiring images, annotating them, training a model, and testing it with live inference. While our focus will be on object detection, the workflows for segmentation, classification, and other tasks follow similar principles (for more details, see [Ultralytics Tasks](https://docs.ultralytics.com/tasks/) in your own time).

![Introduction](./assets/intro.gif)

We will use a system based on the [YOLO](https://en.wikipedia.org/wiki/You_Only_Look_Once) algorithm, which is a state-of-the-art method for real-time object detection. YOLO is particularly lightweight, usually offers good performance, and requires few images for training, making it a particularly useful tool for a variety of applications in computer vision and scientific image analysis.

We will apply this to our USB microscopes and train a model to automatically recognize different kinds of seeds and spices from your kitchen 🫘.

![seeds_overview](./assets/seeds.png)

## Microscope Setup

To train and test your object detection model, you will need:

- A USB microscope, or similar device
- Some seeds to capture images of (e.g., quinoa, chia)
- Python installed on your system (you can do the [Python setup](./sections/training.md#python-setup) at a later stage)

![Camera Setup](./assets/camera_setup.png)

You should also be able to start the camera and capture images.

`````{tab-set}
````{tab-item} Windows
Open the `Camera` app from the Start menu.
````
````{tab-item} Mac
Open the `Photo Booth` app from the Applications folder.
````
````{tab-item} Linux
1. Install [Cheese](https://en.wikipedia.org/wiki/Cheese_(software)) using `sudo apt install cheese`.
2. Launch it from the terminal with the `cheese` command.
````
`````

## Overview

In this workshop, you'll have an opportunity to practice a standard computer vision workflow, which includes the steps illustrated in the diagram below.

```{mermaid}
flowchart LR
    A(🔬 Acquisition) --> B(🖌️ Annotation)
    B --> C(🎓 Training)
    C --> D(⚖️ Validation)
    D --> E(🔋 Inference)
```

Now that you're set up, let's dive in - starting with acquiring some training images.