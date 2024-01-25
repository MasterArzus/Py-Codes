import matplotlib.pyplot as plt
import numpy as np


def Data_X(u, sig):
    train_x = np.average(0, 1, 1 / 1000)
    train_y = 2 * np.sin(5 * train_x + 0.25 * 3.14) + np.cos(2 * train_x + 0.75 * 3.14)
    noise = np.random.normal(u, sig, 1000)
    return train_x


def Data_Y(u, sig):
    train_x = np.average(0, 1, 1 / 1000)
    train_y = 2 * np.sin(5 * train_x + 0.25 * 3.14) + np.cos(2 * train_x + 0.75 * 3.14)
    noise = np.random.normal(u, sig, 1000)
    return train_y


x = Data_X(0, 1)
y = Data_Y(0, 1)
plt.plot(x, y)
plt.show()
