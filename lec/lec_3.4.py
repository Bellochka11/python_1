# АЛГОРИТМЫ БЫСТРАЯ СОРТИРОВКА
def quick_sort(array):
    if len(array) <=1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([5,9,21,6,21,48,954,3]))
print(quick_sort([5,6,3]))