data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data)) # фильтрует значения если условие выполнилось выводит значения с true
print(res) # [0, 2, 4, 6, 8]