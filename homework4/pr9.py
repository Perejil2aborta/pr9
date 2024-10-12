numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break

    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        number = int(user_input)
        numbers.append(number)
    else:
        print("Пожалуйста, введите корректное целое число.")

even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = sum(1 for num in numbers if num % 2 != 0)

print("Количество четных элементов:", even_count)
print("Количество нечетных элементов:", odd_count)
