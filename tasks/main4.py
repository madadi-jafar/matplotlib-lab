import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)
data = np.random.normal(50, 10, 1000)
plt.hist(data,bins = 20,color = "purple",edgecolor = "lightgreen")
plt.xlabel("x",size = 20)
plt.ylabel("y",size = 20)
plt.title("Histogram")
plt.show()