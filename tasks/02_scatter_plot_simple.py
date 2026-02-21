# Difficulty: Easy
# Task: Generate 50 random (x, y) points. Create a scatter plot with red circles.
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)
# TODO: Make scatter plot with red "o" markers


# make
plt.scatter(x, y, color = 'red', marker ='o')

# show
plt.show()