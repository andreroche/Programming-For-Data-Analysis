# Side by Side plots in Python using numpy and mathplotlib. André Roche 10-Oct-18. GMIT course videos

import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 2, 1) # 1 row and 2 columns of plots, i want to select the 1st plot and in it display the next line 
x = np.random.normal (0.0, 1.0, 10000) # mean 0.0, stdev = 1.0 and 10000 samples
plt.hist(x, bins = 20)


plt.subplot(1, 2, 2) # same as above but this time we are selecting the second plot 
x = np.random.uniform (-3.0, 3.0, 10000)
plt.hist(x, bins = 20)


plt.show()