# Difficulty: Intermediate
# Task: Generate random 5x5 correlation matrix. Plot annotated heatmap.
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(4)
# TODO: Create valid corr matrix and heatmap with annotations
data = np.random.rand(5, 5)
corr_matrix = np.corrcoef(data)
plt.imshow(corr_matrix)
for (i, j), z in np.ndenumerate(corr_matrix):
    plt.text(j, i, '{:0.2f}'.format(z), ha='center', va='center')
    
plt.colorbar()
plt.show()