from typing import Callable
import cupy as np
import matplotlib.pyplot as plt
from cupy.typing import ArrayLike
from matplotlib.colors import LinearSegmentedColormap

from .utils import wl2rgb


class SpatialSlice:
    def __init__(
            self,
            spectrum: ArrayLike,
            delta: ArrayLike,
            z: float = 0,
            wavelength: float = 550e-9,
    ):
        self.spectrum = np.asarray(spectrum)
        self.delta = np.asarray(delta)
        self.shape = np.asarray(self.spectrum.shape)
        self.z = float(z)
        self.wavelength = float(wavelength)

        y = np.fft.fftfreq(self.shape[0], delta[0])
        x = np.fft.fftfreq(self.shape[1], delta[1])
        # noinspection PyTypeChecker
        self.u, self.v = np.meshgrid(x, y)

    @classmethod
    def from_field(cls, field, delta, z=0, wavelength=550e-9):
        spectrum = np.fft.fft2(np.fft.ifftshift(field))
        return cls(
            spectrum=spectrum,
            delta=delta,
            z=z,
            wavelength=wavelength,
        )

    def to_field(self):
        return np.fft.fftshift(np.fft.ifft2(self.spectrum))

    @property
    def physical_shape(self):
        return self.shape * self.delta

    def propagate(self, dz):
        k = 1 / self.wavelength
        kz = 2 * np.pi * np.sqrt(k ** 2 - self.u ** 2 - self.v ** 2 + 0j)
        self.spectrum *= np.exp(1j * kz * dz)
        self.z += dz

    def apply_transform(self, trans: Callable[[ArrayLike], None]):
        field = np.fft.fftshift(np.fft.ifft2(self.spectrum))
        trans(field)
        self.spectrum = np.fft.fft2(np.fft.ifftshift(field))

    def draw(self, field=True, phase=False, log_scale=False, show_color=False, data=None):
        """
        field: bool - True为光场（空间域），False为频谱
        log_scale: bool - 是否对幅值取log10
        show_color: bool - 是否显示实际颜色波形，否则热力图显示
        """
        if data is not None:
            pass
        elif field:
            data = self.to_field()
        else:
            data = np.fft.fftshift(self.spectrum)

        if show_color:
            cmap = LinearSegmentedColormap.from_list(
                "monochrome", ["black", wl2rgb(self.wavelength)]
            )
        else:
            cmap = "viridis"

        if phase:
            data = np.angle(data).get()
            cmap = "twilight_shifted"
        else:
            data = np.abs(data).get()

        physical_shape = self.physical_shape.get()
        im = plt.imshow(
            data,
            extent=(0, physical_shape[1], 0, physical_shape[0]),
            cmap=cmap,
            norm="log" if log_scale else None,
        )

        return im
