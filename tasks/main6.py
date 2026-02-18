import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 100, 100)
y = np.sqrt(x)
plt.plot(x,y,marker = "o",markersize = 10,color = "black")
plt.xlabel("x",size = 20)
plt.ylabel("y",size = 20)
plt.title("Funcation",size = 20)
plt.savefig("c:/Users/Mahdi Siwa/Desktop/matplotlib/matplotlib-lab/tasks/sqrt_plot.png",dpi = 150,bbox_inches = "tight")
plt.show()