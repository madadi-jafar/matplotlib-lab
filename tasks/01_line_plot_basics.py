# Difficulty: Easy
# Task: Plot y = x² for x in [0, 10]. Add title, x-label, y-label, and grid.
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
y = x ** 2
# TODO: Create and show the plot

#Sulotion: Task1:

# Create the plot
plt.plot(x, y, color='tab:blue', linewidth=2, marker='o', markersize=5)

# Add title and labels
plt.title('Plot of y = x²')
plt.xlabel("x graph")
plt.ylabel("y graph")

# Add grid 
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()