# Difficulty: Easy
# Task: Plot y = sqrt(x) for x in [0, 100]. Save as "sqrt_plot.png" at 150 DPI.
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 100, 100)
y = np.sqrt(x)
# TODO: Plot and save figure
plt.plot(x, y)
plt.savefig("C:/Users/DELL/Desktop/matplotlib/matplotlib-lab/tasks/task7squarePlot.png", dpi=150)
plt.show()