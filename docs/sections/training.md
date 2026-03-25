# Train your model

```{margin}
Estimated time for this step: 20-25 minutes.
```

To train a model, we will use the YOLO implementation from the [Ultralytics](https://ultralytics.com/) Python library, which provides a variety of tools to train, validate, and work with YOLO models.

## Python setup

You should already have Python installed on your system. We recommend using a fresh Python virtual environment to follow best practices (for more details, see our [Python setup guide](https://epfl-center-for-imaging.github.io/python-setup/)).

```{admonition} Verify your installation
Run `python -V` in your terminal to display your Python version. It should be `3.11` or higher.
```

<!-- ![Python Version](../assets/python_version.gif) -->

Next, install the `ultralytics` library in your Python environment:

```
pip install "ultralytics[solutions]"
```

The `[solutions]` option is used to install a few additional dependencies, including [Streamlit](https://streamlit.io/), which we will use for running live inference in a web browser.

```{admonition} Verify your installation
Run `yolo checks` in your terminal. This command should display some information about the installed package.
```

For advanced or custom installation of Ultralytics, refer to their [Quickstart Guide](https://docs.ultralytics.com/quickstart/).

````{dropdown} (Optional) Test a pre-trained model on your webcam
At this point, if your laptop has a webcam, you should be able to run a pre-trained model, for example `yolo26n.pt`, which is capable of detecting 80 common classes (chair, person...) on your webcam's video stream. To try this out, run the following command:
```
yolo predict model=yolo26n.pt source=0 show=True
```
*Note*: `source=0` represents your webcam as a source for prediction.
````

## Create a `dataset.yaml`

To train a model, you also need to create a YAML configuration file named `dataset.yaml`. This file should specify the paths to your training and validation images, as well as the class labels for your model.

Here’s an example of a minimal `dataset.yaml` file:

```yaml
# Object class names
names:
    0: Quinoa seed
    1: Chia seed

# Dataset directory
path: /home/user/yolo-workshop/dataset
train: images/train
val: images/val
```

You can create your own `dataset.yaml` file and save it somewhere on your computer (for example in your `dataset` folder, to keep things tidy).

## Start training

Once you haver your configuration file, you can start the training process by running the following command in your terminal:

```
yolo detect train data=path/to/dataset.yaml model=yolo26n.pt epochs=200 project=/path/to/output
```

This command specifies:

- `data`: the path to your YAML configuration file.
- `model`: the pre-trained YOLO model you want to fine-tune ([docs](https://docs.ultralytics.com/models/yolo26/)).
- `epochs`: the number of training iterations (higher values mean longer training times).
- `project`: where to save the training outputs.

If you wanted, you could customize many more training parameters ([docs](https://docs.ultralytics.com/modes/train/)).

Once training begins, grab a coffee and watch the progress in the terminal ☕.

![training_progress](../assets/training_progress.png)

```{note}
- Notice that you are not training a model from scratch, but rather **fine-tuning** an existing model (`yolo26n.pt`). This model was pre-trained on a large corpus of natural images (the [COCO](https://cocodataset.org/#home) dataset) and could already detect 80 object classes (chair, person, etc.). Fine-tuning a model is generally a more effective way (more robust, converges faster) to learn to detect new objects than training a completely new model from scratch.
- The `project` folder you selected to save the training outputs should contain a few overviews of the training batches (*train_batch--.jpg*). Note that the training images are modified in scale, orientation, brightness, and undergo other types of transforms. Introducing these [data augmentations](https://docs.ultralytics.com/guides/yolo-data-augmentation/) during training helps the model generalize to a wider range of conditions than the limited set represented in the training images.
```

When the training completes, the results will be saved in the directory you've specified as `project`. These results include:

- Visualizations of predictions on the training and validation datasets.
- [Performance metrics](https://docs.ultralytics.com/guides/yolo-performance-metrics/), such as confusion matrices.
- Training and validation loss curves.
- A record of the training parameters.

Most importantly, there should be a `weights` subfolder in the training outputs. It should contain two model weight files in PyTorch format:

- **`best.pt`**: The model weights from the epoch with the best validation score.
- **`last.pt`**: The model weights from the final training epoch.

These weight files are what you need to reload your model and run it on new images.

```{admonition} Do you need a GPU for training?
While having a GPU can significantly speed up the training process, it is not strictly necessary. YOLO models, especially the smaller ones, can often be trained even on a laptop.
```

Next, you'll test your trained model in real time on the microscope!