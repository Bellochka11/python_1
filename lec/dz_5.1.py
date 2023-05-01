# Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
def fac(n):
    if n == 1:
        return 1
    return  n * fac(n - 1)

def trian(n):
    if n == 1:
        return 1
    return  n + fac(n - 1)
 
 

n = int(input('Введите число: '))
print(f'Факториал равен: {fac(n)} ')
print(f'Треугольное число равно: {trian(n)}')