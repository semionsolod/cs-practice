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

def change_vector(values):
    a = np.array(values, dtype=float).copy()

    a[2:5] = 99
    a[::2] = -1

    return a.tolist()

def cap_above(values, limit):
    
    r = np.array(values, dtype=float).copy()

    r[r > limit] = limit


def celsius_to_fahrenheit(values):
    c = np.array(values, dtype=float)
    f = c* 9 / 5 + 32

    return f.tolist()

    return f.tolist()
