list_1 = []
for i in range(5): # выводим числа от 1 до 4
    list_1.append(i)
    print(list_1)

list_1 = []
print(list_1)
for i in range(5): # выводим числа от 1 до 4
    list_1.append(i) # добавляет каждый элемент в конец
    print(list_1)

list_1 = [1,2,3,4,5,7]
print(list_1.pop()) # удаляет последний элемент в конце. выведет 7
print(list_1) # выведет 1,2,3,4,5

list_1 = [1,2,3,4,5,7]
print(list_1.pop(0)) # удаляет элемент под индексом. выведет 1
print(list_1) # выведет 2,3,4,5,7

list_1 = [1,2,3,4,5,7]
print(list_1.insert(2, 11)) # добавляет 11 элемент на 2 индекс
print(list_1) # выведет 1,2,11,3,4,5,7