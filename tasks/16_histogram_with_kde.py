# Difficulty: Intermediate
# Task: Plot histogram + KDE + theoretical PDF for gamma distribution.
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma, gaussian_kde
np.random.seed(5)
data = gamma.rvs(a=2, scale=2, size=1000)
# TODO: Overlay histogram, PDF, and KDE
