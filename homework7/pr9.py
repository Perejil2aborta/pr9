numbers = [float(x) for x in input("Введите список чисел через пробел: ").split()]

if numbers:
    last_element = numbers[-1]
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]
    numbers[0] = last_element

    print("Список после циклического сдвига вправо:", numbers)
else:
    print("Список пуст.")
