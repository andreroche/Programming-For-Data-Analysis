# Adding titles, legends and lables to plots. André Roche 10-Oct-2018. GMIT course videos


import matplotlib.pyplot as plt  # import the plot package. the plt is just a make upey word/ nickname
import numpy as np 

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0

noise = np.random.normal(0.0, 1.0, len(x))  # centred on 0, stdev = 1.0


plt.plot(x, y + noise, 'r.', label = "Actual") # label = is because of legend added below 
plt.plot(x, y, 'b-', label = "Model") # label = is because of legend added below

plt.title ("Simple Plot")
plt.xlabel("Weight")
plt.ylabel("Mass")
plt.legend() # add a legend to the plot but if you do then you must add label to both plots above 

plt.show()
