# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 0  # Задайте самостоятельно, выбрав произвольное число

s = 0
for item in [el for el in numbers if el > a]:
    s += item

# for item in numbers:
#     if item > a:
#         s += item
print(s)
