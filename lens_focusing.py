"""
透镜聚焦示例
演示透镜如何将平行光束聚焦到焦点
"""

import cupy as np
import matplotlib.pyplot as plt
from angular_spectrum import create_circle, create_lens, SpatialSlice, figure_shape
from angular_spectrum.field import create_spherical_wave

plt.rcParams["font.sans-serif"] = ["SimHei"]


def lens_focusing():
    """透镜聚焦演示"""
    lens_r = 2.5e-2
    hole_r = 2.5e-3
    physical_shape = np.array((2 * lens_r, 2 * lens_r))
    shape = np.array((2048, 2048))
    delta = physical_shape / shape

    wave_length = 550e-9
    focal_length = 50e-2
    # spot = 550e-9
    L1 = 100e-2
    L2 = 100e-2

    color = True
    phase = False

    field = np.zeros(shape.tolist(), dtype=complex)
    # create_circle(field, physical_shape / 2, spot, delta=delta)
    create_spherical_wave(field, wave_length, delta)

    plane = SpatialSlice.from_field(field, physical_shape / shape, 0, wave_length)
    plt.figure(figsize=figure_shape(shape, 3))

    plt.subplot(1, 3, 1)
    plane.draw(show_color=color, phase=phase)

    plt.subplot(1, 3, 2)
    plane.propagate(L1)
    plane.apply_transform(
        lambda f: (
            create_lens(f, wave_length, focal_length, delta),
            create_circle(f, physical_shape / 2, hole_r, 0, delta),
            create_circle(f, physical_shape / 2, lens_r, 0, delta, reverse=True),
        )
    )
    plane.draw(show_color=color, phase=phase)

    plt.subplot(1, 3, 3)
    plane.propagate(L2)
    plane.draw(show_color=color, phase=phase)

    plt.tight_layout()

    plt.savefig("output/lens_focusing.png")
    plt.show()


if __name__ == "__main__":
    lens_focusing()
