# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
#  3 3 2 12 (каждое число вводится с новой строки)
import random

a_1 = int(input("Введите размер массива 1: "))
a_2 = int(input("Введите размер массива 2: "))

mass_1 = []
for el_2 in range(a_1):
    mass_1.append(random.randint(-10, 10))
print(mass_1)

mass_2 = []
for el_2 in range(a_2):
    mass_2.append(random.randint(-10, 10))
print(mass_2)

mass_3 = []

for i in mass_1: # бежим i в массиве 1. пробегаемся конкретно в массиве по элементам
    if i not in mass_2: # если i нет в массиве 2
        mass_3.append(i) # добавляем в 3 массив те значения из массива 1, которых нет в массиве 2
print(mass_3)



