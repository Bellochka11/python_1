
def mylt(x, y):
    return x * y 
def calc(op, a, b):
    print(op(a, b))



def sum(x, y):
    return x + y
# ⇔ (равносильно) строчки 9,10 и 12 можно записать так и так
sum = lambda x, y: x + y
calc(sum,5,45) # сюда мы передаем значение из sum, можно записать в одну строчку как на 16 


calc(lambda a,b: a + b, 5, 45) # самый короткий способ вызвать функцию