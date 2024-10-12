import random


def generate_ticket():
    ticket = []
    numbers = list(range(1, 26))
    random.shuffle(numbers)

    for i in range(5):
        ticket.append(numbers[i * 5:(i + 1) * 5])

    return ticket


ticket = generate_ticket()

print("Ваш лотерейный билет:")
for row in ticket:
    print(row)

user_choices = []
for i, row in enumerate(ticket):
    while True:
        try:
            choice = int(input(f"Выберите число из строки {i + 1}: {row} "))
            if choice in row:
                user_choices.append(choice)
                break
            else:
                print("Пожалуйста, выберите число из предложенных в строке.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

app_choices = [random.choice(row) for row in ticket]

print("Ваш выбор:", user_choices)
print("Выбор приложения:", app_choices)
