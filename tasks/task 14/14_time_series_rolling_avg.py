# Difficulty: Intermediate
# Task: Plot noisy time series + 7-day rolling average with shaded std band.
import matplotlib.pyplot as plt
import numpy as np
days = np.arange(100)
signal = 10 + np.sin(days/10) * 5
noise = np.random.normal(0, 1, 100)
data = signal + noise
# TODO: Plot raw data, rolling avg, and uncertainty band
avg = np.convolve(data, np.ones(7)/7, mode='same')
std = np.std([np.roll(data, i) for i in range(7)], axis=0)

plt.plot(days, data, alpha=0.3, label='Raw')
plt.plot(days, avg, 'r', label='7d Avg')
plt.fill_between(days, avg - std, avg + std, color='r', alpha=0.2)
plt.legend()
plt.show()