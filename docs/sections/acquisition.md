# Create a training set of images

```{margin}
Estimated time for this step: 10-15 minutes.
```

You should start by collecting a set of representative images of the objects you'd like to detect. For a first try, we recommend that you take **five** images for training and **two** for validation. You should vary the "scene" by placing different objects in the field of view for each image. You can keep the magnification fixed between the images.

![training_set](../assets/training_set.png)

Organize your images into a dedicated folder named `dataset` on your computer. Within this folder, create a subfolder called `images`, and further divide it into `train` for training images and `val` for validation images. The file names don't matter. Tou can save the images in either `png`, `jpeg`, or `tif` format (they should be RGB colored images).

Here’s an example of how your dataset folder structure should look:

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
```

```{admonition} Tips for acquiring a good training set


- The more images, the better. That said, when you fine-tune your model from a generalist pretrained model (as opposed to training from scratch), which is usually the standard, you probably won't need a ton of images (the exact amount varies based on the task and project). To introduce a new object for detection in  natural images, having at least 20-30 example views of that new object is a good rule of thumb.  
- The more **variety**, the better. Your training set should reflect the conditions under which the model will operate. For instance, if variations in illumination, focus, or magnification are expected during deployment, similar variations should be present when capturing your training images.
```
