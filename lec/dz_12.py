# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

import random

a = int(input('Введите всего чисел '))

array = [random.randint(0, 9) for i in range(a)]
print(array, end = ",")

b = int(input("\n Введите число X: "))

min = near = 10

for i in range(0, len(array)):
  diff = abs(b - array[i]) # abc это модуль
  if diff < min:
    min = diff
    near = array[i]

print(near)