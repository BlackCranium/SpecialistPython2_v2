from base_sort import sort_choice
# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]

sort_choice(numbers)

s = sum(numbers[-5:])
print(s)
