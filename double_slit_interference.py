"""
双缝干涉示例
演示两个矩形狭缝产生的干涉现象
"""

import cupy as np
import matplotlib.pyplot as plt
from angular_spectrum import create_rectangle, figure_shape, SpatialSlice

plt.rcParams["font.sans-serif"] = ["SimHei"]


def double_slit_interference():
    """双缝干涉演示"""
    physical_shape = np.array((1e-3, 1e-3))
    shape = np.array((4096, 4096))
    delta = physical_shape / shape

    slit_size = np.array((0.5e-3, 0.005e-3))
    wave_length = 530e-9
    L = 5e-3
    d = 0.05e-3

    field = np.zeros(shape.tolist())
    offset = np.r_[0, d / delta[1]]
    create_rectangle(field, (shape - offset) / 2, slit_size / delta)
    create_rectangle(field, (shape + offset) / 2, slit_size / delta)

    plane = SpatialSlice.from_field(field, physical_shape / shape, 0, wave_length)
    plt.figure(figsize=figure_shape(shape, 2))

    plt.subplot(1, 2, 1)
    plane.draw(show_color=True)

    plt.subplot(1, 2, 2)
    plane.propagate(L)
    plane.draw(show_color=True)

    plt.tight_layout()

    plt.savefig("output/double_slit_interference.png")
    plt.show()


if __name__ == "__main__":
    double_slit_interference()
