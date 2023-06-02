colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

with open('file.txt', 'w') as data: # первый параметр это текстовый файл второй режим это режим. data это название к файлу
    data.write('line 1\n')
    data.write('line 2\n') # значения перезаписываются

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line) # напечатает в консоль то что находится в файле txt
data.close()

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()