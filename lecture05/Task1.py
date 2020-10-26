import random

n = 20

numbers = []
for _ in range(n):
    numbers.append(int(random.randint(1, 10)))
print('Изначальный список:')
print(numbers)
sort = sorted(numbers)

b_numbers = []
a_numbers = []

a = sort[-1]
b = sort[0]

# Исключение наибольшего элемента

for i in range(n):
    if a != numbers[i]:
        a_numbers.append(numbers[i])
print('Вывод списка без максимального:')
print(a_numbers)

# Исключение наименьшего элемента

for i in range(n):
    if b != numbers[i]:
        b_numbers.append(numbers[i])
print('Вывод списка без минимального:')
print(b_numbers)