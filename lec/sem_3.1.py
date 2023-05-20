# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.
a = [1, 1, 2, 0, -1, 3, 4, 4]
b = []
for temp in a:
    if(not temp in b): # добавили те значения которых нету в b. если туда добавили первую 1, то вторая 1 не входит!!
        b.append(temp)
print(len(b)) # вывели длину списка
print(len(set(a))) # 2 решение set это каждый элемент уникален (повторяться не может) множество!! преобразовали список в множество и вывели длину

