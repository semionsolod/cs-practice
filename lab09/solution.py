import numpy as np

def make_hours():
    return np.arange(0, 22, 3).tolist()


def vector_report(values):
    n = np.array(values, dtype=float)
    return {
        "third": float(n[2]),
        "last": float(n[-1]),
        "middle": n[2:6].tolist(),
        "every_second": n[::2].tolist(),
        "reversed": n[::-1].tolist(),
    }
