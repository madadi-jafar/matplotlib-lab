import matplotlib.pyplot as plt
import numpy as np
x =np.array([1, 2, 3, 4, 5])
y =np.array([2.1, 3.9, 6.2, 7.8, 10.1])
yerr =np.array([0.2, 0.3, 0.4, 0.25, 0.35])
m,b = np.polyfit(x,y,1)
y_pred = m*x+b
plt.errorbar(x,y,yerr = yerr,capsize=5,capthick=2,color ="black",marker = ".")
plt.plot(x,y_pred,color = "yellow")
plt.show()