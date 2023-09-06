# Входной массив: [4, 3, 2, 4, 1, 3, 2]
# В данной задаче вы должны найти способ найти одиночное число с использованием массивов и алгоритмов.

def find_single_number(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num, freq in count.items():
        if freq == 1:
            return num

arr = [4, 3, 2, 4, 1, 3, 2]
single_number = find_single_number(arr)
print(f"The single number is: {single_number}")