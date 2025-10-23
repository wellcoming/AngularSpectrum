from colour import wavelength_to_XYZ, XYZ_to_sRGB
import numpy as np


def wl2rgb(wavelength):
    wl = wavelength * 1e9
    if not 360 < wl < 780:
        return 0, 0, 0
    xyz = wavelength_to_XYZ(wl)  # 先转CIE XYZ
    srgb = XYZ_to_sRGB(xyz)  # 转sRGB色彩空间
    return np.clip(srgb, 0, 1)


def figure_shape(shape, n):
    tmp = tuple(shape.get() * (1.2 / 100))
    return round(tmp[0] * n), round(tmp[1])
