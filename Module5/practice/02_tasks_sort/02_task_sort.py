# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = -10  # Задайте самостоятельно, выбрав произвольное число
b = 10  # Задайте самостоятельно, выбрав произвольное число

s = 0
# for item in [el for el in numbers if a < el < b]:
#     s += item

for item in numbers:
    if b > item > a:
        s += item
print(s)
