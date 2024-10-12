import math

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))


if a > b:
    a, b = b, a  

a_int = math.ceil(a)
b_int = math.floor(b)

kvadrati = [i**2 for i in range(a_int, b_int + 1)]

print("Квадраты целых чисел между", a, "и", b, ":", kvadrati)
