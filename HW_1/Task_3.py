# У вас есть массив целых чисел, в котором каждое число, кроме одного, повторяется дважды. 
# Вам нужно найти это одиночное число.

def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Пример использования
array = [1, 2, 3, 2, 1]
single_number = find_single_number(array)
print(f"The single number is: {single_number}")