import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
ax.set_title('График')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()

x = np.linspace(-5, 5, 100)
# x = np.linspace(1)
y = x ** 2 + 4
ax.plot(x, y)

plt.show()