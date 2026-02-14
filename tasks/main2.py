import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x,y,
            color = "red",
            marker = "o")
plt.show()