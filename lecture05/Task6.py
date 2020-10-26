import random

n = 20

numbers = []
for i in range(n):
    numbers.append(random.uniform(0, 10))
    numbers[i] = int(numbers[i] * 1000) / 1000
print('Изначальный список:')
print(numbers)

sort = sorted(numbers)
max = sort[-1]
o_numbers = []

for i in range(n):
    if numbers[i] != max:
        o_numbers.append(numbers[i])
    else:
        break
print('Вывод списка до максимального элемента:')
print(o_numbers)
