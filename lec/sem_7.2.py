# Дан список, вывести отдельно буквы и цифры используя filter
# ввод [12, 'fsfs', 574] 
# вывод ['fsfs'], [12, 574]

list_1  = [12, 'fsfs', 574] 
print(list_1)
res_list_1 = list(filter(lambda x: type(x) == int, list_1)) #  записываем в рес1 значения типа инт
res_list_2 = list(filter(lambda x: type(x) != int, list_1)) # записываем в рес2 значения типа не инст
print(res_list_1, res_list_2)