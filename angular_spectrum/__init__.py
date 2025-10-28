"""
Angular Spectrum Method for Optical Propagation
用于光学传播的角谱方法库
"""

from .wavefront import SpatialSlice
from .field import create_rectangle, create_circle, create_lens
from .utils import wl2rgb, figure_shape

__all__ = [
    "SpatialSlice",
    "create_rectangle",
    "create_circle",
    "create_lens",
    "wl2rgb",
    "figure_shape",
]

__version__ = "1.0.0"
