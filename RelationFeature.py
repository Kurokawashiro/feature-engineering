#  how to tell if two features A&B are related or not with the label C
#  for example: feature_plot(data.A, data.B, data.label)
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def feature_plot(data1, data2, label):

    label = np.array(list(label))

    plt.figure(figsize=(14, 8))
    plt.scatter(data1, data2, c=label)
    plt.xlabel(data1.name)
    plt.ylabel(data2.name)
    plt.show()

#  ------------------------------------------------------------------------
#  This is a more detailed one with seaborn, let's assume type(data) == Dataframe
first_n_features = 10
feature_data = data[:, :first_n_features]
col = feature_data.columns
corr = feature_data.corr()
threshold = 0.5
cor_list = []
for i in range(first_n_features):
    for j in range(i+1, first_n_features):
        if (corr.iloc[i, j] > threshold and corr.iloc[i, j] < 1) or (corr.iloc[i, j] < -threshold and corr.iloc[i, j] > -1):
            cor_list.append([corr.iloc[i, j], i, j])

for v, i, j in cor_list:
    sns.pairplot(data, hue=data.label, size=6, x_vars=col[i], y_vars=col[j])
    plt.show()



