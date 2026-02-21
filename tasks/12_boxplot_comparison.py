# Difficulty: Intermediate
# Task: Compare 3 groups using boxplots. Add notches and custom colors.
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
A = np.random.normal(70, 10, 100)
B = np.random.normal(75, 5, 100)
C = np.random.exponential(10, 100) + 60
# TODO: Create grouped boxplot
