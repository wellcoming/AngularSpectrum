![AngularSpectrum](https://socialify.git.ci/wellcoming/AngularSpectrum/image?custom_description=%E5%9F%BA%E4%BA%8E%E8%A7%92%E8%B0%B1%E6%B3%95%E7%9A%84%E7%AE%80%E6%B4%81%E5%85%89%E5%AD%A6%E4%BC%A0%E6%92%AD%E5%BA%93%E3%80%82&description=1&forks=1&issues=1&language=1&name=1&pulls=1&stargazers=1&theme=Auto)

[![](https://img.shields.io/github/license/SeSePerson/SeSePerson)](https://www.gnu.org/licenses/gpl-3.0.html) [![Python](https://img.shields.io/badge/Python-%E2%89%A53.9-blue.svg)](https://www.python.org/) [![CuPy](https://img.shields.io/badge/CuPy-%E2%89%A512-0a7bbb.svg)](https://cupy.dev/) [![matplotlib](https://img.shields.io/badge/matplotlib-%E2%89%A53.10.7-11557c.svg)](https://matplotlib.org/) [![colour-science](https://img.shields.io/badge/colour--science-%E2%89%A50.4.6-ff7f0e.svg)](https://www.colour-science.org/) [![Build](https://img.shields.io/badge/build-hatchling-8A2BE2.svg)](https://hatch.pypa.io/latest/) [![GPU](https://img.shields.io/badge/GPU-CUDA%20ready-76B900.svg)](https://developer.nvidia.com/cuda-zone) [![OS](https://img.shields.io/badge/OS-any-lightgrey.svg)](https://pypi.org/classifiers/)

---

## Angular Spectrum

基于角谱法（Angular Spectrum Method）的简洁光学传播库。支持构造常见光阑/相位元件并在频域传播，适合教学与快速实验。

### 安装

```bash
pip install -e .
```

CuPy 建议按平台选择合适发行版（如 `cupy-cuda12x`）。

### 快速上手

```python
import cupy as np
from angular_spectrum import SpatialSlice, create_rectangle

shape = np.array((1024, 1024))
physical = np.array((1e-3, 1e-3))
delta = physical / shape

field = np.zeros(shape.tolist())
create_rectangle(field, physical / 2, np.array((0.2e-3, 0.01e-3)), delta=delta)

plane = SpatialSlice.from_field(field, delta, wavelength=550e-9)
plane.propagate(1e-3)
plane.draw(show_color=True)
```

### 依赖

- Python ≥ 3.9
- CuPy ≥ 12（或对应 CUDA 版本包）
- matplotlib ≥ 3.10.7
- colour-science ≥ 0.4.6

### 许可

GPL-3.0
