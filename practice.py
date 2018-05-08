import tensorflow as tf
import os
import numpy as np
from skimage import data as sd
import matplotlib.pyplot as plt

def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory)
                    if os.path.isdir(os.path.join(data_directory, d))]

    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f)
                        for f in os.listdir(label_directory)
                        if f.endswith(".ppm")]

        for f in file_names:
            images.append(sd.imread(f))
            labels.append(int(d))
        return images, labels

ROOT_PATH = "\Coding\TrafficSigns"
train_data_directory = os.path.join(ROOT_PATH, "Training")
test_data_directory = os.path.join(ROOT_PATH, "Testing")

images, labels = load_data(train_data_directory)

images2 = np.array(images)
labels2 = np.array(labels)
print(images2.ndim)
print(images2.size)
images[0]

plt.hist(labels2, 62)
plt.show
