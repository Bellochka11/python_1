# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# 1 5 2 1 5 4
# 1 1 2 1 1 4
from random import randint

n1_set = list(randint(1, 5) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n1_set)
def change (list):
    min_num = min(list)
    max_num = max(list)
    for i in range(len(list)):
        if list[i] == max_num:
            list[i] = min_num
    return list

print(change(n1_set))