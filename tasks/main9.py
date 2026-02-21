import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors
np.random.seed(2)
x = np.random.randn(100)
y = np.random.randn(100)
colors = x + y
plt.scatter(x,y,c = colors )
plt.colorbar(label ='Intensity')
plt.show()