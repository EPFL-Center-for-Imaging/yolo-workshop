# Annotate your images

```{margin}
Estimated time for this step: 20-25 minutes.
```

In this step, you'll annotate the images you've collected for training and validation. Annotation consists in manually creating a "ground truth" for the model to learn from. For object detection, this means drawing rectangular bounding boxes around the objects. Moreover, you can assign class labels to these bounding boxes to categorize them.

There are many tools available for image annotation ([Label Studio](https://github.com/HumanSignal/label-studio), [CVAT](https://github.com/cvat-ai/cvat), [Napari](https://forum.image.sc/t/napari-plugin-for-creating-object-detection-training-data/80622), [QuPath](https://gitlab.com/epfl-center-for-imaging/qupath-yolo-toolbox)...). For simplicity, we'll use [Make Sense](https://www.makesense.ai/), a free and open-source web-based tool.

![annotations overview](../assets/annotations.png)

1. Open [Make Sense](https://www.makesense.ai/) in your web browser and click "Get Started" to create a new project.
2. Upload your images (both training and validation) and select the "Object Detection" task.
3. Provide a list of class labels ("quinoa seed", "chia seed"...) for your objects. Then, select "Start project."
4. It is then time to draw bounding boxes around your objects! Try you annotate all discernable objects. It's good if you can draw boxes accurately, however they don't need to be pixel-perfect. Try to spend a few minutes per image at most.
5. Once you've annotated all of your images, save your annotations by navigating to `Actions > Export Annotations`. Choose the option to export **A .zip package containing files in YOLO format**.
6. Download and unzip the package. You should see text files (`image_00.txt`, `image_01.txt`, ...) corresponding to each image's annotations.
7. Move the text files into a `labels` subfolder alongside your images (respectively under `train` and `val`). Your dataset structure should look similar to this:

```
dataset
|---- images
     |---- train
          |---- image_01.png
          |---- image_02.png
          |---- ...
          |---- image_05.png
     |---- val
          |---- image_01.png
          |---- image_02.png
|---- labels
     |---- train
          |---- image_01.txt
          |---- image_02.txt
          |---- ...
          |---- image_05.txt
     |---- val
          |---- image_01.txt
          |---- image_02.txt
```

With your annotated dataset ready, you're all set to train your first model.