#  how to tell if two features A&B are related or not with the label C
#  for example: feature_plot(data.A, data.B, data.label)
import matplotlib.pyplot as plt
import numpy as np


def feature_plot(data1, data2, label):

    label = np.array(list(label))

    plt.figure(figsize=(14, 8))
    plt.scatter(data1, data2, c=label)
    plt.xlabel(data1.name)
    plt.ylabel(data2.name)
    plt.show()
