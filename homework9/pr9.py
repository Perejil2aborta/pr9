import re


def parse_email(email):
    pattern = r'^(?P<username>[^@]+)@(?P<domain>[^@]+\.[^@]+)$'

    match = re.match(pattern, email)

    if match:
        username = match.group('username')
        domain = match.group('domain')
        return username, domain
    else:
        return None, None


def main():
    email = input("Введите ваш email: ")

    username, domain = parse_email(email)

    if username and domain:
        print(f"Имя пользователя: {username}")
        print(f"Доменное имя: {domain}")
    else:
        print("Ошибка: неверный формат email. Убедитесь, что есть хотя бы одна точка после символа '@'.")


main()
