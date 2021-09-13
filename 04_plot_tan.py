import numpy as np
import matplotlib.pylab as plt

x = np.linspace(-np.pi, np.pi, 100)
y_tan = np.tan(x)

plt.plot(x, y_tan, label='tangent')

plt.title('tan')
plt.xlabel('x [rad]')
plt.ylabel('y')
plt.ylim([-5, 5])
plt.axis('tight')
plt.legend()
plt.show()