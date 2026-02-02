import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([2021, 2022, 2023, 2024, 2025])

y1 = np.array([10, 15, 13, 17, 20])
y2 = np.array([8, 12, 14, 16, 18])
y3 = np.array([6, 10, 12, 14, 17])

# Plot lines (visuals customized inside plot())
plt.plot(
    x, y1,
    color='tab:blue',
    linestyle='-',
    linewidth=3,
    marker='o',
    markersize=9,
    markerfacecolor='white',
    markeredgewidth=2,
    label='Student A'
)

plt.plot(
    x, y2,
    color='tab:green',
    linestyle='--',
    linewidth=3,
    marker='s',
    markersize=9,
    markerfacecolor='white',
    markeredgewidth=2,
    label='Student B'
)

plt.plot(
    x, y3,
    color='tab:orange',
    linestyle='-.',
    linewidth=3,
    marker='^',
    markersize=9,
    markerfacecolor='white',
    markeredgewidth=2,
    label='Student C'
)

# Show plot
plt.legend()
plt.show()