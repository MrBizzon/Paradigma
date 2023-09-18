import numpy as np

def pearson_correlation(x, y):
    # Проверяем, что длины массивов совпадают
    if len(x) != len(y):
        raise ValueError("Длины массивов должны совпадать")
    
    # Вычисляем средние значения массивов
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    # Вычисляем сумму произведений отклонений от средних значений
    sum_product_deviations = np.sum((x - mean_x) * (y - mean_y))
    
    # Вычисляем сумму квадратов отклонений от средних значений
    sum_x_deviations_squared = np.sum((x - mean_x) ** 2)
    sum_y_deviations_squared = np.sum((y - mean_y) ** 2)
    
    # Вычисляем корреляцию Пирсона по формуле
    pearson_correlation = sum_product_deviations / np.sqrt(sum_x_deviations_squared * sum_y_deviations_squared)
    
    return pearson_correlation

# Пример использования
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = pearson_correlation(x, y)
print('Корреляция Пирсона: %.2f' % correlation)