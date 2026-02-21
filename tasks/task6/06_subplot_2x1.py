# Difficulty: Easy
# Task: Create 2 subplots (2 rows, 1 col): sin(x) and cos(x) for x in [0, 2π].
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 100)
# TODO: Make 2 subplots with proper labels

fig, (ax1, ax2) = plt.subplots(2, 1)

# Plot sin(x) 
ax1.plot(x, np.sin(x))
ax1.set_title('Sine Wave')
ax1.set_ylabel('sin(x)')

# Plot cos(x) 
ax2.plot(x, np.cos(x))
ax2.set_title('Cosine Wave')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')

# Adjust layout and display
plt.tight_layout()
plt.show()
