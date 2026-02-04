import matplotlib.pyplot as plt
import numpy as np

years = np.array([2021, 2022, 2023, 2024, 2025])
scores = np.array([10, 15, 13, 17, 20])

plt.bar(
    years,
    scores,
    width=0.6,
    alpha=0.9,
    edgecolor='black',
    linewidth=1,
    label='Student A'
)

plt.xlabel('Year')
plt.ylabel('Score')
plt.title('Student A Scores by Year')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()

plt.show()
