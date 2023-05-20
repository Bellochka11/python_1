# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
text = input("Введите текст: ").lower() #lower() Переводит в нижний регистр т.к. Маша и маша это одинаковые слова
unique_words = set(text.split()) # сет делает множество. во множестве только уникальные значения. сплит разделяет строку на отдельные слова
print("Количество различных слов:", len(unique_words)) # длина множества ответ т.к. нету повторяющихся элементов

