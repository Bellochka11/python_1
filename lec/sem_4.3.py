# Ваня и Петя поспорили, кто быстрее решит 
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не 
# такими смышлеными. Никто из ребят не смог до 
# конца сделать это задание. Они решили так: у кого 
# будет меньше ошибок в коде, тот и выиграл спор. За 
# помощью товарищи обратились к Вам, студентам.

number = int(input("Введите цифру: "))
maxNumber = number 

while (number != 0):
    if (number > maxNumber):
        maxNumber = number
    number = int(input("Введите цифру: "))
# maxNumber = number if number > maxNumber else maxNumber

print(f"Максимальный элемент: {maxNumber}")


number = maxNumber = int(input("Введите цифру: "))

while (number != 0):
#if (number > maxNumber):
# maxNumber = number
    maxNumber = number if number > maxNumber else maxNumber
    number = int(input("Введите цифру: "))

print(f"Максимальный элемент: {maxNumber}")
