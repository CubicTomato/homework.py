# Ввод числа и операции(й), а также проверка коректности

try:
    s = int(input('Введите положительное целое число *При переводе в римские до 3999*: '))
except ValueError:
    print('Введите положительное целое.')
    exit(1)

print ('Операции перевода: \n"bin": в двоичную \n"hex": в шестнадцатиричную \n"roman": в римские')
action = input('Выбор операции перевода *можно несколько через ","*: ').split(',')

for i in range(len(action)):
    action[i] = action[i].strip()
    if action[i] == 'roman' and not(s <= 3999):
        print('Вы ввели число больше 3999 для перевода в римское число')
        exit(2)

# Класс обработчик

class Number:
    def __init__(self, number):
        self.n = number
        self.result = 'Результата нет'

    def bin(self):
        num = self.n
        bin_n = []
        def bin_inner(in_bin_n):
            if in_bin_n != 1:
                k = in_bin_n // 2
                bin_n.append(str(in_bin_n % 2))
                return bin_inner(k)
            else:
                bin_n.append(str(in_bin_n))
        bin_inner(num)
        bin_n.reverse()
        self.result = ''.join(bin_n)
        return self.result

    def hex(self):
        self.result = ''
        hex_numb_dict = {'F': 15, 'E': 14, 'D': 13, 'C': 12, 'B': 11, 'A': 10}
        hex_numb = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
        num = self.n
        hex_n = []

        def convert_hex(n):
            nonlocal hex_numb_dict
            if not(n < 10):
                for key, value in hex_numb_dict.items():
                    if n == value:
                        hex_n.append(key)
            else:
                hex_n.append(str(n))
            return None

        def hex_inner(in_hex_n):
            nonlocal hex_numb
            nonlocal hex_numb_dict
            if not(in_hex_n in hex_numb):
                k = in_hex_n // 16
                c = in_hex_n % 16
                convert_hex(c)
                return hex_inner(k)
            else:
                convert_hex(in_hex_n)
        hex_inner(num)
        hex_n.reverse
        hex_n1 = ''.join(hex_n)
        return hex_n1

    def roman(self):
        roman_numb = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                      'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        num = self.n
        self.result = ''

        while num != 0:
            for key, value in roman_numb.items():
                if num < value:
                    continue
                else:
                    k = num // value
                    self.result = self.result + k * key
                    if value == 1:
                        num = num - value
                        break
                    else:
                        num = num % value
                        break
        return self.result

n = Number(s)

# Вывод результата

for elem in action:
    if elem == 'bin':
        print('Число ' + str(s) + ' в бинарной системе: ' + str(s) + ' = ' + str(n.bin()))
    elif elem == 'hex':
        print('Число ' + str(s) + ' в шестнадцатиричной системе: ' + str(s) + ' = ' + str(n.hex()))
    elif elem == 'roman':
        print('Число ' + str(s) + ' в римскими цифрами: ' + str(s) + ' = ' + str(n.roman()))
    else:
        print('Вы ввели неверную операцию перевода.')
