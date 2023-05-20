#  Напишите программу, которая на вход принимает два числа A и B, и возводит число
# А в целую степень B с помощью рекурсии.

def degree (a, b, c):
    if b != 0:
        c *= a
        b -= 1
    else:
        return c
    return degree(a, b, c)

num1 = int(input("Введи число А: "))
num2 = int(input("Введи число Б: "))
c = 1
print(degree(num1, num2, c))


# def my_power(a,b):
#     if b ==0:
#         return 1
#     else:
#         return a* my_power(a,b-1)

# a= int(input())
# b= int(input())
# print(my_power(a,b))


