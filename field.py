import cupy as np


def create_rectangle(field: np.ndarray, pos, size, intensity=1.0):
    pos = np.asarray(pos)
    size = np.asarray(size)

    lt = np.round(pos - size / 2).astype(int)
    rb = np.round(pos + size / 2).astype(int) + 1

    lt = np.clip(lt, 0, np.asarray(field.shape))
    rb = np.clip(rb, 0, np.asarray(field.shape))

    field[lt[0]: rb[0], lt[1]: rb[1]] = intensity


def create_circle(field: np.ndarray, pos, size, intensity=1.0):
    pos = np.asarray(pos).reshape(2, 1, 1)
    size = np.asarray(size).reshape(2, 1, 1)

    tmp = (np.indices(field.shape) - pos) / size
    dist_sq = np.sum(tmp ** 2, axis=0)
    field[dist_sq <= 1] = intensity
