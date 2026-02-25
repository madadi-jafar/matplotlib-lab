import matplotlib.pyplot as plt
import numpy as np
np.random.seed(4)
data = np.random.rand(100,5)
corr_matrix = np.corrcoef(data,rowvar =False)
fig,ax = plt.subplots(figsize = (6,6))
im = ax.imshow(corr_matrix,cmap='coolwarm')
plt.colorbar = (im)
for i in range (len(corr_matrix)):
    for j in range (len(corr_matrix)):
        text = ax.text(j,i,f'{corr_matrix[i,j]:.2f}',ha = "center",va ="center",color = "black")

ax.set_xticks(np.arange(5))
ax.set_yticks(np.arange(5))
ax.set_xticklabels(['V1','V2','V3','V4','V5'])
ax.set_yticklabels(['V1','V2','V3','V4','V5'])
plt.show()