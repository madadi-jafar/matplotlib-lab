import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 50)
y = x ** 2
fig = plt.figure(figsize = (12,5))
with plt.style.context("dark_background"):
    ax1 = fig.add_subplot(1,2,1)
    ax1.bar(x,y,color = 'tab:green')
    ax1.set_title('Style:seaborn')
with plt.style.context("ggplot"):
    ax2 = fig.add_subplot(1,2,2)
    ax2.scatter(x,y,color = 'tab:red')
    ax2.set_title('Style:default')
plt.tight_layout()
plt.show()