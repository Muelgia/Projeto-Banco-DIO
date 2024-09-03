import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3, 4, 100)
y = x**3-2*x**2+12*x-1
plt.plot(x, y)
plt.show()