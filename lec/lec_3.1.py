# ФУНКЦИИ
# Необходимо создать функцию sumNumbers(n), которая будет 
# считать сумму всех элементов от 1 до n.
def sum_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)

sum_numbers(5)


def sum_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum # если программа видит ретерн то завершает работу функции

print(sum_numbers(5))



def sum_numbers(n, y = "Hello"):
    print(y)
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print(sum_numbers(5, 'qwert')) # выведет qwert а не hello т.к. перезаписали значение

def sum_str(*args):    # * значит что неограниченное кол-во аргументов
    res = ''
    for i in args:
        res += i
    return res
    
print(sum_str('q', 'w', 'e'))
print(sum_str('q', 'w', 'e', 'l', 'r', 'f'))