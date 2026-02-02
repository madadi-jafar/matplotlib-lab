import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([2021, 2022, 2023, 2024, 2025])

y1 = np.array([10, 15, 13, 17, 20])
y2 = np.array([8, 12, 14, 16, 18])
y3 = np.array([6, 10, 12, 14, 17])

# ---------------- Common properties (shared) ----------------
common_props = {
    'linewidth': 3,
    'markersize': 9,
    'markerfacecolor': 'white',
    'markeredgewidth': 2,
    'alpha': 0.9
}

# ---------------- Individual line properties ----------------
line1_props = {
    'color': 'tab:blue',
    'linestyle': '-',
    'marker': 'o',
    'label': 'Student A'
}

line2_props = {
    'color': 'tab:green',
    'linestyle': '--',
    'marker': 's',
    'label': 'Student B'
}

line3_props = {
    'color': 'tab:orange',
    'linestyle': '-.',
    'marker': '^',
    'label': 'Student C'
}

# ---------------- Plot ----------------
plt.plot(x, y1, **common_props, **line1_props)
plt.plot(x, y2, **common_props, **line2_props)
plt.plot(x, y3, **common_props, **line3_props)

plt.legend()
plt.show()
