import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 20)
plt.plot(x,x,color = "blue",label = "y=x",marker = ".",ms = 10,mec = "yellow",markerfacecolor = "black",linewidth = 2)
plt.plot(x,2*x,linestyle = "dashed",color = "green",label = "y = 2x",marker = "*",ms  =5,mec  ="red",mfc = "purple",linewidth = 2)
plt.xlabel("x",color = "black",size = 30)
plt.ylabel("y",color = "black",size  =30)
plt.title("Funcations:(x,2x)",color = "black",size = 30)
plt.legend()
plt.show()