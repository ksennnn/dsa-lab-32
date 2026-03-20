import sys

# Считывание массива из параметров командной строки
try:
    arr = list(map(int, sys.argv[1:]))
except ValueError:
    print("Ошибка: введите целые числа через пробел")
    sys.exit(1)

if not arr:
    print("Массив пуст")
else:
    original_arr = arr.copy()
    
    # Поиск повторяющихся элементов
    duplicates = [num for num in set(arr) if arr.count(num) > 1]
    
    # Преобразование элементов
    for i in range(len(arr)):
        if arr[i] < 10:
            arr[i] = 0
        elif arr[i] > 20:
            arr[i] = 1
    
    # Вывод результатов
    if duplicates:
        print(f"Повторяющиеся элементы: {duplicates}")
    else:
        print("Повторяющиеся элементы отсутствуют")
    
    print(f"Исходный массив: {original_arr}")
    print(f"Преобразованный массив: {arr}")
    