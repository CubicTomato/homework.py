import random

n = 20

numbers = []
for _ in range(n):
    numbers.append(int(random.randint(0, 10)))
print('Изначальный список:')
print(numbers)

o_numbers = []

for i in range(n):
    if numbers[i] != 0:
        o_numbers.append(numbers[i])
print('Вывод списка без 0:')
print(o_numbers)
