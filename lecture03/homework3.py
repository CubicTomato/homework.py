# Ввод

g = input('Введите число градусов и вид: ')
a = list(g)
*numb, last = a
n = ''.join(numb)

# Проверка корректности

if not(n.isdecimal()):
    print('Введите число градусов')
    exit(1)
if not(last == 'F' or last == 'f' or last == 'C' or last == 'c'):
    print('Введите вид градусов')
    exit(2)

# Преобразование

n = float(n)
if last == 'f' or last == 'F':
    n = (n - 32) * 5/9
    fl = 1
else:
    n = (n * (9/5)) + 32
    fl = 2

# Вывод

if fl == 1:
    print(str(n) + 'C')
else:
    print(str(n) + 'F')
