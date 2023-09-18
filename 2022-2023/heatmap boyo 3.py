import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,12,15,16]])
ax = sns.heatmap(data, linewidth = 0.5, cmap='coolwarm')
plt.show()
