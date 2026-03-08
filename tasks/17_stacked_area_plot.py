# Difficulty: Intermediate
# Task: Plot stacked area chart for 4 energy sources over 10 years.
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(6)
years = range(2015, 2025)
sources = np.cumsum(np.random.rand(4, 10) * 10, axis=1)
# TODO: Create stacked area plot with legend
