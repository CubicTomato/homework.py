n = str(input('Введите число больше 2: '))

# Блок проверки

if not(n.isdigit()):
    print('Введите число целое число')
    exit (1)
else:
    n = int(n)
if n < 2:
    print('Введите число больше 1')
    exit (1)

# Блок вычислений

i = 2
s = []
while i < n:
    s.append(int(i))
    i += 1
else:
    s.append(int(n))

q = 2
while 2 * q <= n:
    y = 2 * q
    q += 1
    del s[s.index(y)]

q = 2
while 3 * q <= n:
    y = 3 * q
    q += 1
    if y in s:
        del s[s.index(y)]

q = 2
while 5 * q <= n:
    y = 5 * q
    q += 1
    if y in s:
        del s[s.index(y)]

q = 2
while 7 * q <= n:
    y = 7 * q
    q += 1
    if y in s:
        del s[s.index(y)]

# Блок вывода

with open('Prime_Numbers.txt', 'w') as f:
    f.write('Это все простые числа от 2 до ' + str(n) + ':\n')
    for i in range(len(s)):
        f.write(str(s[i]) + '\n')

print('Программа закончила свою работу, результат представлен в файле.')