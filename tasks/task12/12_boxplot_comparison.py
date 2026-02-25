# Difficulty: Intermediate
# Task: Compare 3 groups using boxplots. Add notches and custom colors.
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
A = np.random.normal(70, 10, 100)
B = np.random.normal(75, 5, 100)
C = np.random.exponential(10, 100) + 60
# TODO: Create grouped boxplot

all_data = [A,B,C]
colors = ["#DE1616FF", "#0400F0", "#F1F11B"]
boxplot = plt.boxplot(all_data,notch=True,patch_artist=True)
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
    
plt.xticks([1,2,3],['A','B','C'])
plt.show()