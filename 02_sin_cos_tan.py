import numpy as np

a = np.sin(np.pi/6.)
b = np.cos(np.pi/3.)
c = np.tan(np.pi/4.)

print(a)
print(b)
print(c)

angles = np.deg2rad(np.array((0., 30., 45., 60., 90.)))
sines = np.sin(angles)
print(sines)