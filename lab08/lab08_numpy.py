import numpy as np

hours = np.arange(0,22,3)
line = np.linspace(0,1,5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2,3), -1)
identity = np.identity(3)

print("hours:", hours, "shape:", hours.shape, "ndim:", hours.ndim,\
      "size:", hours.size, "dtype:", hours.dtype)
