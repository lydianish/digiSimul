import numpy as np
import math
from PIL import Image
from scipy import interpolate
from random import uniform
import cv2
from scipy import interpolate

def func(x, y):
    return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]
print(grid_y)
points = np.random.rand(1000, 2)
print(points)
print(points.shape)
values = func(points[:,0], points[:,1])
grid_z2 = interpolate.griddata(points, values, (grid_x, grid_y), method='cubic')
print(grid_z2)
print(grid_z2.shape)


import matplotlib.pyplot as plt
plt.subplot(221)
plt.imshow(func(grid_x, grid_y).T, extent=(0,1,0,1), origin='lower')
plt.imshow(grid_z2.T, extent=(0,1,0,1), origin='lower')
plt.title('Cubic')
plt.gcf().set_size_inches(6, 6)
plt.show()