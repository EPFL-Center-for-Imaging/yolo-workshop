# Object Detection with YOLO

In this workshop, we'll go through the steps of acquiring images, annotating them, training an object detection model, and testing it in real time on our USB microscopes.

```{mermaid}
flowchart LR
    A(🔬 Acquisition) --> B(🖌️ Annotation)
    B --> C(🎓 Training)
    C --> D(⚖️ Validation)
    D --> E(🔋 Inference)
```

![Introduction](./assets/intro.gif)

We will implement a system based on the [YOLO](https://en.wikipedia.org/wiki/You_Only_Look_Once) algorithm, which is a state-of-the-art method for real-time object detection. YOLO models usually offer good performance and require few images for training, making them particularly useful for applications in computer vision and scientific image analysis.

We will train a model to automatically recognize different kinds of seeds and spices from your kitchen:

![seeds_overview](./assets/seeds.png)

## Microscope Setup

To complete this workshop, you will need:

- A USB microscope
- Some seeds to capture images of (e.g., quinoa, chia)
- Python installed on your system

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

Now that you're set up, let's dive in - starting with acquiring some training images.