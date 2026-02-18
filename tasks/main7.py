import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
figure,axes = plt.subplots(2,1)

axes[0].plot(x,x*2,color = "yellow")
axes[0].set_title('sin(x)',loc ="left",color = "blue",size = 20)


axes[1].plot(x,x**2,color = "green")
axes[1].set_title("cos(x)",loc = "left",color = "blue",size = 20)

plt.show()