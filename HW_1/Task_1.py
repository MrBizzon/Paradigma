# Задача №1

# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для сортировки числа
# в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

from typing import List


def sort_array(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError(
            'На вход должен подаваться непустой целочисленный список')
    return sorted(arr, reverse=True)


lst = [randint(0, 100) for i in range(7)]
print(lst)
print(sort_array(lst))