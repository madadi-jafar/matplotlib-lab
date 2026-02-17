# Difficulty: Easy
# Task: Plot y = x² for x in [0, 10]. Add title, x-label, y-label, and grid.
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
y = x ** 2
# TODO: Create and show the plot

#create
plt.plot(x,y)

#show
plt.show()