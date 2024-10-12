numbers = [float(x) for x in input("Введите список чисел через пробел: ").split()]

if numbers:
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

    print("Изменённый список:", numbers)
else:
    print("Список пуст.")
