# Histograms in Python using numpy and mathplotlib. André Roche 10-Oct-18. GMIT course videos

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal (0.0, 1.0, 1000)

plt.hist(x, bins = 20)

plt.show()
