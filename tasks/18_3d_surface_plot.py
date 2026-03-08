# Difficulty: Hard
# Task: Plot 3D surface z = sin(sqrt(x²+y²)). Add colorbar, labels, and viewing angle.
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
# TODO: Create full 3D surface plot
