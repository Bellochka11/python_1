# Напишите программу которая на вход принимает вещественное число и показывает сумму его цифр 
# ввод 1.23 вывод 6

number = input('Введите вещественное число: ')
print(number)
number = number.replace(',', '') # убрали запятую и пробел
number = number.replace('.', '')
print(number)
result = sum(map(lambda x: int(x), number)) # перевели каждый элемент в инт и просуммировали
print(result)