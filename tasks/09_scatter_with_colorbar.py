# Difficulty: Intermediate
# Task: Scatter plot where color = x + y. Add colorbar labeled "Intensity".
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(2)
x = np.random.randn(100)
y = np.random.randn(100)
colors = x + y
# TODO: Create scatter with colormap and colorbar
