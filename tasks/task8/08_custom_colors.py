# Difficulty: Easy
# Task: Plot y = x with blue line, y = 2x with green dashed line. Add legend.
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 20)
# TODO: Plot two lines with custom styles and legend
    
plt.plot(x,x, color = 'blue',label = 'y=x')

plt.plot(x,2*x, 'k--', color ='green', label = 'y=2x')

plt.legend()

plt.show()