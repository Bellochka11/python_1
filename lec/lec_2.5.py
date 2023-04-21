d = {} # создали пустой словарь
d = dict() # создали пустой словарь
d['q'] = 'qwerty' # создали ключ q, по которому если обратимся получим qwerty
print(d)
d['w'] = 'werty' # создали второй ключ w, по которому если обратимся получим werty
print(d)
print(d['w']) # вывели значение из ключа w: werty

a = {}
a ={'up': 'верх', 'down': 'вниз'}
print(a) # выведет {'up': 'верх', 'down': 'вниз'}
print(a['up']) # выведет верх

a[890] = 4322 # добавили еще ключ
print(a) # выведет {'up': 'верх', 'down': 'вниз', 890: 4322}
del a['up'] # удаление элемента
print(a)

for i in a:
    # print(i)
    print('{}: {}'.format(i,a[i])) # вывели значения через двоеточие

print(a.items()) # вывел список где каждый элемент кортеж 1 знач ключ 2 значение из словаря

slovar = {"1": "one", "2": "two"} # создали словарь
print(slovar)
slovar["privet"] = "hello" # добавили в словарь ключ и значение
print(slovar)
for i in slovar:
    print(i) # выведет только ключи 1 2 privet
for i in slovar:
    print(i, slovar[i]) # выведет и ключи и значения!
for (key, value) in slovar.items():
    print(key, value) # выведет и ключи и значения!

spisok = []
for key, value in slovar.items():
    spisok.append([key,value])
print(spisok) # список в списке [['1', 'one'], ['2', 'two'], ['privet', 'hello']] ключ, значение
