import arrow_plot

import numpy as np
import matplotlib.pyplot as plt

n = 10
    
plt.clf()

x = np.random.random(n)
y = np.random.random(n)
arrow_plot.arrow_plot(plt,x,y)

plt.show()