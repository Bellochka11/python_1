print(5)
print(5, 8, 7)
n = 5
print(n)
b = None # пустое значение
print(b) # вывел пустое значение, то есть None
s = 1.85
print(s)
print(type(s)) # указывает тип данных
q = 'qw\'er'
print(q) # выведет qw'er
w = 'qw"qw"er'
print(w) # выведет qw"qw"er
l = 5.56
print(l) # 5.56
p = int(l)
print(p) # 5

#ИНТЕРПОЛЯЦИЯ 
t = 5
y = 4.1
u = 'hello'
print(t,y,u) # 5 4.1 hello
print(f"{t} - {y} - {u}") # 5 - 4.1 - hello
print("{} - {} - {}".format(t,y,u)) # 5 - 4.1 - hello