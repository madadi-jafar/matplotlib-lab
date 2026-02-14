import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
y = x ** 2
plt.plot(x,y)
plt.title("Square funcation",
          fontsize =20,
          family = "Arial",
          fontweight ="bold",
          color = "blue")
plt.xlabel("X",
           fontsize = 30,
           family = "Arial",
          fontweight ="bold",
          color = "green")
plt.ylabel("Y",
              fontsize =30,
           family = "Arial",
          fontweight ="bold",
          color = "green")
plt.grid(axis = "both")
plt.show()