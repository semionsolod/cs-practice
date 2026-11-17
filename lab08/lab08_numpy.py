import numpy as np

hours = np.arange(0,22,3)
line = np.linspace(0,1,5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2,3), -1)
identity = np.identity(3)

print("Задание 1")
print("hours:", hours, "shape:", hours.shape, "ndim:", hours.ndim,\
      "size:", hours.size, "dtype:", hours.dtype)

print()
print("Задание 2")
print('третий элемент:', hours[2])
print('последний элемент:', hours[-1])
print('2-5:', hours[2:6])
print('через 2:', hours[::2])
print('обратно:', hours[::-1])

