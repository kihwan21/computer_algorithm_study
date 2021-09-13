import numpy as np

print(np.pi)               # pi = 3.14...

a = np.deg2rad(90)         # x * pi / 180
b = np.rad2deg(np.pi/2)    # 180 * x / pi

print(a)    # 1.57...
print(b)    # 90.0

angles = np.deg2rad(np.array((0., 30., 45., 60., 90.)))
print(angles) # [0.         0.52359878 0.78539816 1.04719755 1.57079633]