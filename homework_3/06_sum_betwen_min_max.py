# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

import random

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0
for i in range(1, len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

print(f'Левая граница: {array[idx_min]}\nПравая граница: {array[idx_max]}')

summ = 0
for i in range(idx_min + 1, idx_max):
    summ += array[i]
print(f'Сумма = {summ}')
