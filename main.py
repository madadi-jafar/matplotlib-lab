import matplotlib.pyplot as plt
import numpy as np

years = np.array([2021, 2022, 2023, 2024, 2025])

student_a = np.array([10, 15, 13, 17, 20])
student_b = np.array([8, 12, 14, 16, 18])
student_c = np.array([6, 10, 12, 14, 17])

bar_width = 0.25
x = np.arange(len(years))

plt.bar(x - bar_width, student_a, width=bar_width, label='Student A')
plt.bar(x,             student_b, width=bar_width, label='Student B')
plt.bar(x + bar_width, student_c, width=bar_width, label='Student C')

plt.xticks(x, years)
plt.xlabel('Year')
plt.ylabel('Score')
plt.title('Student Scores Comparison')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()

plt.show()
