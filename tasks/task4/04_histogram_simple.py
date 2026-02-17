# Difficulty: Easy
# Task: Generate 1000 normal samples (mean=50, std=10). Plot histogram with 20 bins.
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)
data = np.random.normal(50, 10, 1000)
# TODO: Plot histogram

# draw
plt.hist(data, bins=20)

# show
plt.show()

