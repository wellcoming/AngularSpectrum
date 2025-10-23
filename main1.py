# import numpy as np
import cupy as np
import matplotlib.pyplot as plt

from field import create_circle
from wavefront import SpatialSlice
from utils import figure_shape

plt.rcParams["font.sans-serif"] = ["SimHei"]

physical_shape = np.array((0.7e-3, 0.7e-3))
shape = np.array((4096,4096))
delta = physical_shape / shape

wave_length = 530e-9
r = 0.01e-3
L = 1.2e-3

color = False

field = np.zeros(shape.tolist())
create_circle(field, shape / 2, r / delta)

plane = SpatialSlice.from_field(field, physical_shape / shape, L, wave_length)
plt.figure(figsize=figure_shape(shape,2))

plt.subplot(1, 2, 1)
plane.draw(show_color=color)

plt.subplot(1, 2, 2)
plane.propagate(L)
plane.draw(show_color=color)

plt.tight_layout()

plt.savefig('ans1.png')
plt.show()
