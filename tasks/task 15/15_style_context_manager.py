# Difficulty: Intermediate
# Task: Compare "seaborn" vs "default" style side-by-side using context manager.
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 50)
y = x ** 2
# TODO: Use plt.style.context in subplots
for i, s in enumerate(['default', 'seaborn-v0_8']):
    with plt.style.context(s):
        ax = plt.subplot(1, 2, i + 1)
        ax.plot(x, y, label=s)
        ax.legend()

plt.show()