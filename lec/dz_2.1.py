#  На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
# n = int(input()) #всего монет
# count_zero = 0 #орел
# count_one = 0 #решка
# for i in range(n):
#     x = int(input()) #вводим монеты
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
#     if count_one > count_zero:
#         print(count_zero)
# else:
#     print(count_one)

vsego = int(input("введите всего монет: "))
orel = 0
reshka = 0
for i in range(vsego):
    x = int(input())
    if(x == 0):
        orel += 1
    else:
        reshka+=1
    if(orel > reshka):
        print(reshka)
else:
    print(orel)