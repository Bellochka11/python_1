# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# 0 1 1 2 3 5 8
# a1a2a3a4a5a6a7

a = int(input("Введите число: "))
pred = 0 
next = 1
n = 2
while next <= a:
    pred = next
    next = pred + next
    n+=1
print(n)


# a = int(input("Введите число: "))
# if a == 0:
#     print(1)
# else:
#     fib_prev, fib_next = 0, 1
#     n = 2
#     while fib_next <= a:
#         if fib_next == a:
#             print(n)
#             break
#         fib_prev, fib_next = fib_next, fib_prev + fib_next
#         n += 1
#     else:
#         print(-1)