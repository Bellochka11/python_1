# В некоторой школе решили набрать три новых 
# математических класса и оборудовать кабинеты для 
# них новыми партами. За каждой партой может сидеть 
# два учащихся. Известно количество учащихся в 
# каждом из трех классов. Выведите наименьшее 
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

print('Введите кол-во учащихся в 1 классе')
a = int(input())
print('Введите кол-во учащихся в 2 классе')
b = int(input())
print('Введите кол-во учащихся в 3 классе')
c = int(input())
e = int(((a+b+c)/2) + 0.9999)
print(f'Наименьшее кол-во парт: {e}')