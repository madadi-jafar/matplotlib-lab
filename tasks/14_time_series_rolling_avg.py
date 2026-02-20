# Difficulty: Intermediate
# Task: Plot noisy time series + 7-day rolling average with shaded std band.
import matplotlib.pyplot as plt
import numpy as np
days = np.arange(100)
signal = 10 + np.sin(days/10) * 5
noise = np.random.normal(0, 1, 100)
data = signal + noise
# TODO: Plot raw data, rolling avg, and uncertainty band
