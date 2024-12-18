import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 20)
y = np.linspace(0, 1, 20)

plt.plot(x, y)
plt.xlabel("Mn(tf-m)")
plt.ylabel("Pn(tf)")
plt.grid()
plt.show()
