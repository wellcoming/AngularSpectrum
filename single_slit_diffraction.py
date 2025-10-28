"""
单缝衍射示例
演示单个矩形狭缝产生的衍射现象
"""

import cupy as np
import matplotlib.pyplot as plt
from angular_spectrum import create_rectangle, SpatialSlice, figure_shape

plt.rcParams["font.sans-serif"] = ["SimHei"]


def single_slit_diffraction():
    """单缝衍射演示"""
    physical_shape = np.array((0.7e-3, 0.7e-3))
    shape = np.array((4096, 4096))
    delta = physical_shape / shape
    slit_size = np.array((0.5e-3, 0.01e-3))

    wave_length = 530e-9
    L = 1.2e-3

    color = True

    field = np.zeros(shape.tolist())
    create_rectangle(field, physical_shape / 2, slit_size, delta=delta)

    plane = SpatialSlice.from_field(field, physical_shape / shape, 0, wave_length)
    plt.figure(figsize=figure_shape(shape, 2))

    plt.subplot(1, 2, 1)
    plane.draw(show_color=color)

    plt.subplot(1, 2, 2)
    plane.propagate(L)
    plane.draw(show_color=color)

    plt.tight_layout()

    plt.savefig("output/single_slit_diffraction.png")
    plt.show()


if __name__ == "__main__":
    single_slit_diffraction()
