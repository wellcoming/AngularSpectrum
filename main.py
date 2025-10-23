import cupy as np
import matplotlib.pyplot as plt

from field import create_rectangle
from utils import figure_shape
from wavefront import SpatialSlice

plt.rcParams["font.sans-serif"] = ["SimHei"]

physical_shape = np.array((1e-3, 1e-3))
shape = np.array((2048,2048))
delta = physical_shape / shape

slit_size = np.array((0.5e-3, 0.01e-3))
wave_length = 530e-9
L = 1.2e-3
d = 0.1e-3

field = np.zeros(shape.tolist())
offset = np.r_[0, d / delta[1]]
create_rectangle(field, (shape - offset) / 2, slit_size / delta)
create_rectangle(field, (shape + offset) / 2, slit_size / delta)

plane = SpatialSlice.from_field(field, physical_shape / shape, L, wave_length)
plt.figure(figsize=figure_shape(shape,2))

plt.subplot(1, 2, 1)
plane.draw(show_color=True)

plt.subplot(1, 2, 2)
plane.propagate(L)
plane.draw(show_color=True)

plt.tight_layout()

plt.savefig('ans.png')
plt.show()
