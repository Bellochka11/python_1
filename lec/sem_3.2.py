# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9] k = 3
# Output: [7, 8, 9, 1, 2, 3, 4, 5, 6]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
arr2 = arr[-k:] + arr[:-k] # [7, 8, 9] + [1, 2, 3, 4, 5, 6] с -3 до конца + с начала до -3
print(arr2)
