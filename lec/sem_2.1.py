# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# вход Input: 5
# выход Output: 120
#с начала так (1 2 3 4 5 ):
a = int(input('Введите число: '))
b = 1
result = 1
while b <= a:
    result *= b
    b += 1
print(result)

# с конца решается так с 5 до 1 (5 4 3 2 1 ):
# number = tempNumber= int(input("Введите n : "))
# factorialNumber = 1

# while (tempNumber != 1):
# factorialNumber *= tempNumber
# tempNumber -= 1

# print(f"факториал {number} = {factorialNumber}")