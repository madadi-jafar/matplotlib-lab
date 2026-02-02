import matplotlib.pyplot as plt
import numpy as np

years = np.array([2022,2023,2024,2025,2026])
students = np.array([21, 43,33,9,16])

plt.plot(years, students, marker='o')
plt.show()