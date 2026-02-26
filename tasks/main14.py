import matplotlib.pyplot as plt
import numpy as np
days = np.arange(100)
signal = 10 + np.sin(days/10) * 5
noise = np.random.normal(0, 1, 100)
data = signal + noise
window = 7
rolling_avg = np.convolve(data,np.ones(window)/window,mode = 'valid')
rolling_std = np.array([np.std(data[i:i+window])for i in range(len(data)-window+1)])
days_adj = days[window-1:]
plt.figure(figsize=(10,6))
plt.plot(days,data,label = 'Row Data',alpha = 1,color = 'black')
plt.plot(days_adj,rolling_avg-rolling_std,rolling_avg+rolling_std,color = 'blue',alpha = 1,label = "Std Dev Band")
plt.legend()
plt.title("Time series analysis")
plt.savefig("c:/Users/Mahdi Siwa/Desktop/New folder (2)/Time series.png",dpi = 300,bbox_inches = "tight")
plt.show()