# Two Plots on one set of axes. André Roche 10-Oct-18. GMIT course videos.

import matplotlib.pyplot as plt  # import the plot package. the plt is just a make upey word/ nickname
import numpy as np 

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0

noise = np.random.normal(0.0, 1.0, len(x))  # centred on 0, stdev = 1.0


plt.plot(x, y + noise, 'r.')
plt.plot(x, y, 'b-')


plt.show()

plt.plot(x, y + noise, 'g.')
plt.plot(x, y, 'y-')


plt.show()