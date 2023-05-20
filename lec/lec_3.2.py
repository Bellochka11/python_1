# МОДУЛЬНОСТЬ
# варианты как вызывать функцию из другого файла 

import modul1
print(modul1.max1(5,9))

from modul1 import max1
print(max1(5,9))

from modul1 import * # * значит что мы хотим импортировать все функции из файла модуль1
print(max1(5,9))

import modul1 as m1 # переименовали модуль1 на м1 чтобы было короткое имя функции
print(m1.max1(5,9))