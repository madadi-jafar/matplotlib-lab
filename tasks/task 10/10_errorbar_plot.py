# Difficulty: Intermediate
# Task: Plot data with error bars. Fit and show linear regression line.
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
yerr = [0.2, 0.3, 0.4, 0.25, 0.35]
# TODO: Plot with error bars and regression line

slope,intercept = np.polyfit(x,y,1)
regression = slope * x + intercept
    
plt.errorbar(x,y, yerr= yerr,fmt ='o', label = 'Errorbar',color = 'red')

plt.plot(x,regression, label=f'Fit: y = {slope:.2f}x + {intercept:.2f}', color = 'black')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Regression plotting & Error bar')

plt.legend()

plt.show()