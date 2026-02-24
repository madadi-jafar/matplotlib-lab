import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
A = np.random.normal(70, 10, 100)
B = np.random.normal(75, 5, 100)
C = np.random.exponential(10, 100) + 60
data =[A,B,C]
box = plt.boxplot(data,patch_artist = True,notch = True)
colors = ["blue","yellow","green"]
for patch,color in zip(box["boxes"],colors):
    patch.set_facecolor(color)
plt.show()