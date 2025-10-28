import cupy as np


def create_rectangle(field: np.ndarray, pos, size, intensity=1.0, delta=(1, 1)):
    delta = np.asarray(delta)
    pos = np.asarray(pos) / delta
    size = np.asarray(size) / delta

    lt = np.round(pos - size / 2).astype(int)
    rb = np.round(pos + size / 2).astype(int) + 1

    lt = np.clip(lt, 0, np.asarray(field.shape))
    rb = np.clip(rb, 0, np.asarray(field.shape))

    field[lt[0]: rb[0], lt[1]: rb[1]] = intensity


def create_circle(field: np.ndarray, pos, size, intensity=1.0, delta=(1, 1), reverse=False):
    delta = np.asarray(delta)
    pos = (np.asarray(pos) / delta).reshape(2, 1, 1)
    size = (np.asarray(size) / delta).reshape(2, 1, 1)

    coords = (np.indices(field.shape) - pos) / size
    dist_sq = np.sum(coords ** 2, axis=0)
    if reverse:
        field[dist_sq > 1] = intensity
    else:
        field[dist_sq <= 1] = intensity


def create_spherical_wave(
        field: np.ndarray,
        wavelength: float,
        delta=(1, 1),
        z0=1e-3,
        waist_ratio: float = 1 / 4
):
    delta = np.asarray(delta).reshape(2, 1, 1)
    shape = np.asarray(field.shape).reshape(2, 1, 1)
    coords = (np.indices(field.shape) - shape / 2)
    dist_sq = np.sum((coords * delta) ** 2, axis=0)

    r = np.sqrt(z0 ** 2 + dist_sq)
    k = 2 * np.pi / wavelength
    phase = np.exp(1j * k * r)

    gaussian_aperture = np.exp(-np.sum((coords / shape / waist_ratio) ** 2, axis=0))
    wave_to_add = gaussian_aperture * phase / r
    wave_to_add /= np.max(np.abs(wave_to_add))
    field += wave_to_add


def create_lens(field: np.ndarray, wavelength: float, focallength: float, delta=(1, 1)):
    delta = np.asarray(delta).reshape(2, 1, 1)
    shape = np.asarray(field.shape).reshape(2, 1, 1)

    coords = (np.indices(field.shape) - shape / 2) * delta
    phase = -np.pi * np.sum(coords ** 2, axis=0) / (wavelength * focallength)
    field *= np.exp(1j * phase)
