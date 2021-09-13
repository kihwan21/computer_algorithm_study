import numpy as np
import matplotlib.pylab as plt

r = 3
theta = np.linspace(0, 2*np.pi, 201)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)

plt.title('Circle')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('square')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()