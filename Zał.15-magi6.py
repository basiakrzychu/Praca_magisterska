# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:34:07 2021

@author: basiakrzychu
"""

import os
from IPython.display import Image, display
from keras.preprocessing.image import load_img
import PIL
from PIL import ImageOps
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
import random
from tensorflow.keras import layers
import tensorflow as tf
import winsound
from keras import backend as K
  
import matplotlib.pyplot as plt


K.clear_session()

input_dir = "scale_images/"
target_dir = "scale_masks_2/"
xx=144
yy=256
img_size = (xx, yy)
num_classes = 3
batch_size = 32


input_img_paths = sorted(
    [
        os.path.join(input_dir, fname)
        for fname in os.listdir(input_dir)
        if fname.endswith(".jpg")
    ]
)
target_img_paths = sorted(
    [
        os.path.join(target_dir, fname)
        for fname in os.listdir(target_dir)
        if fname.endswith(".png") and not fname.startswith(".")
    ]
)

print("Number of samples:", len(input_img_paths))

for input_path, target_path in zip(input_img_paths[:10], target_img_paths[:10]):
    print(input_path, "|", target_path)
    
    
display(Image(filename=input_img_paths[4]))

# Display auto-contrast version of corresponding target (per-pixel categories)
img = PIL.ImageOps.autocontrast(load_img(target_img_paths[4]))
display(img)


class Droga(keras.utils.Sequence):
    """Helper to iterate over the data (as Numpy arrays)."""

    def __init__(self, batch_size, img_size, input_img_paths, target_img_paths):
        self.batch_size = batch_size
        self.img_size = img_size
        self.input_img_paths = input_img_paths
        self.target_img_paths = target_img_paths

    def __len__(self):
        return len(self.target_img_paths) // self.batch_size

    def __getitem__(self, idx):
        """Returns tuple (input, target) correspond to batch #idx."""
        i = idx * self.batch_size
        batch_input_img_paths = self.input_img_paths[i : i + self.batch_size]
        batch_target_img_paths = self.target_img_paths[i : i + self.batch_size]
        x = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32")
        for j, path in enumerate(batch_input_img_paths):
            img = load_img(path, target_size=self.img_size)
            x[j] = img
        y = np.zeros((self.batch_size,) + self.img_size + (1,), dtype="uint8")
        for j, path in enumerate(batch_target_img_paths):
            img = load_img(path, target_size=self.img_size, color_mode="grayscale")
            y[j] = np.expand_dims(img, 2)
            # Ground truth labels are 1, 2, 3. Subtract one to make them 0, 1, 2:
            y[j] -= 1
        return x, y

model = keras.models.load_model("modele/model_144_256.h5",compile=False)



# Split our img paths into a training and a validation set
val_samples = 250
random.Random(2137).shuffle(input_img_paths)
random.Random(2137).shuffle(target_img_paths)
train_input_img_paths = input_img_paths[:-val_samples]
train_target_img_paths = target_img_paths[:-val_samples]
val_input_img_paths = input_img_paths[-val_samples:]
val_target_img_paths = target_img_paths[-val_samples:]

# Instantiate data Sequences for each split
train_gen = Droga(
    batch_size, img_size, train_input_img_paths, train_target_img_paths
)
val_gen = Droga(batch_size, img_size, val_input_img_paths, val_target_img_paths)

 
model.compile(optimizer="rmsprop", loss="sparse_categorical_crossentropy")
 
callbacks = [
    keras.callbacks.ModelCheckpoint("wagi10.h5", save_best_only=True)
]
 
# Train the model, doing validation at the end of each epoch.
epochs = 200
with tf.device('/device:GPU:0'):
  history=model.fit(train_gen, epochs=epochs, validation_data=val_gen, callbacks=callbacks)


print(history.history.keys())
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.show()

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

val_gen = Droga(batch_size, img_size, val_input_img_paths, val_target_img_paths)
val_preds = model.predict(val_gen)


def display_mask(i):
    """Quick utility to display a model's prediction."""
    mask = np.argmax(val_preds[i], axis=-1)
    mask = np.expand_dims(mask, axis=-1)
    img = PIL.ImageOps.autocontrast(keras.preprocessing.image.array_to_img(mask))
    display(img)


# Display results for validation image #10
i = 0
with tf.device('/device:GPU:0'):
# Display input image
  display(Image(filename=val_input_img_paths[i]))

# Display ground-truth target mask
  img = PIL.ImageOps.autocontrast(load_img(val_target_img_paths[i]))
  display(img)

# Display mask predicted by our model
  display_mask(i)  # Note that the model only sees inputs at 150x150.