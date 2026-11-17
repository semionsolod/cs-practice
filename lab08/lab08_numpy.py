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

print()
print('Задание 3')

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print('форма:', temperatures.shape)
print('число измерений:', temperatures.ndim)
print('число элементов:', temperatures.size)
print('2 строка 3 столбец:', temperatures[1,2])
print('1 строка:', temperatures[0, :])
print('последний столбец:', temperatures[:, -1])
print('первые 2 строки без первого столбца:', temperatures[:2, 1:])
print('центральный фрагмент 2х2:', temperatures[0:2, 1:3], 'форма:', \
      temperatures[0:2, 1:3].shape)

print()
print('Задание 4')

matrix = np.arange(1, 26).reshape(5, 5)

print('первые 3 строки:', matrix[:3, :],'shape:', matrix[:3, :].shape)
print('последние 2 строки:', matrix[-2:, :], 'shape:', matrix[-2:, :].shape)
print('первые 2 столбца:', matrix[:, :2], 'shape:', matrix[:, :2].shape )
print('строки 1-3 столбцы 2-4:', matrix[1:4, 2:5], 'shape:', matrix[1:4, 2:5].shape)
print('угловой блок 2х2:', matrix[-2:, -2:], 'shape:', matrix[-2:, -2:].shape)

print()
print('Задание 5')

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()

changed_hours[2:5] = 99
changed_hours[::2] = -1

print('changed_hours:', changed_hours)
print('hours:', hours)
#copy() нужна, чтобы не трогать исходный массив и не ссылаться на него

changed_matrix = matrix.copy()

changed_matrix[1, :]=0
changed_matrix[:, -1]=-1
changed_matrix[1:4, 1:4] = 100

print('changed_matrix:', changed_matrix)
print('matrix:', matrix)

print()
print('Задание 6')

numbers = np.arange(0,12)
table = numbers.reshape(3,4)
transposed = table.T

print('numbers shape:', numbers.shape)
print('table shape:', table.shape)
print('transposed shape:', transposed.shape)

#reshape(3, 4) работает так как число элементов 12, а не 15 как в reshape(5, 3)


