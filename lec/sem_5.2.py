# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
# 5 элементов
# 1 2 3 4 5
# 5 4 3 2 1 вывелось в обратном порядке

def rotate (n):
    if n == 0:
        return " "
    else:
        a = int(input("Value "))
        return rotate(n-1) + f" {a} "

n = int(input("Enter n: "))
print(rotate(n))