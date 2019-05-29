from __future__ import print_function
from tensorflow import keras
import numpy as np

model = keras.models.load_model("data/sf_nn.h5")

print(model.summary())

data_x_test = np.loadtxt('data/input_x_test.csv', dtype=float)
data_y_test = np.loadtxt('data/input_y_test.csv', dtype=float)

loss, acc = model.evaluate(data_x_test, data_y_test)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))
