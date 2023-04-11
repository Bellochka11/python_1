# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 
number = int(input('Введите трехзначное число: '))
if(number > 99 and number < 1000):
     a = int(number % 10)
     b = int(number / 100)
     c = int((number % 100) / 10)
     sum = int(a + b + c)
     print(f"Сумма цифр числа {number} равна {sum}")
else:
     print("Вы ввели не трехзначное число! ")


# input_message = int(input("Введите число: "))
# result = 0
# while input_message > 0:
#     result = result + input_message % 10 # 3 + 2 + 1
#     input_message = input_message // 10 # 12 1
# print(result)
