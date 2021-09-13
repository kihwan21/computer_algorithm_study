import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0, 2*np.pi, 201)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, 'r', label='sin')
plt.plot(x, y_cos, 'b', label='cos')

plt.title('sin vs. cos')
plt.xlabel('x [rad]')
plt.ylabel('y')
plt.axis('tight')
plt.legend()
plt.show()