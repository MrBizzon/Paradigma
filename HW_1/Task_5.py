def find_missing_and_duplicate(arr):
    n = len(arr)
    
    # Формируем сумму чисел от 1 до N (включительно)
    # и сумму квадратов чисел от 1 до N (включительно)
    sum1 = n * (n + 1) // 2
    sum2 = n * (n + 1) * (2*n + 1) // 6
    
    # Разность между фактической суммой массива и sum1 будет пропущенным числом
    missing_num = sum1 - sum(arr)
    
    # Разность между фактической суммой квадратов массива и sum2 будет повторяющимся числом
    duplicate_num = (sum2 - sum([x**2 for x in arr])) // missing_num
    
    return duplicate_num, missing_num

arr = [2, 4, 1, 5, 6, 5]
duplicate, missing = find_missing_and_duplicate(arr)
print('duplicate number:', duplicate)
print("missing number:", missing)