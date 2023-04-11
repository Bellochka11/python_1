# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


input_message = int(input("Введите число: "))
result = 0
while input_message > 0:
    result = result + input_message % 10 # 3 + 2 + 1
    input_message = input_message // 10 # 123 12 1
print(result)