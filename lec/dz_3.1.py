# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2
# a = int(input('Введите всего чисел: '))
# x = int(input('Введите число x: '))
# array = []


import random

a = int(input('Введите всего чисел: '))

array = [random.randint(0, 9) for i in range(a)] # от 0 до 9 рандомные числа 
print(array, end = ",") #разделитель запятая

x = int(input("\n Введите число x: "))

print(array.count(x)) # каунт это кол-во этого числа в нашем случае x