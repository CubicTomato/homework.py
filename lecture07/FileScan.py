import os
from os import path

# Ввод пути к директории (к сожалению, я не смог сделать поиск директории, потому только полный путь)

print('Чтобы сравнить результаты с данными не из документа "Scaned_Dir_File.txt", в конце ввода пути к директории введите "?".')
s = input('Введите полный путь к директории сканирования: ')

old_dir = os.getcwd()

fl2 = 0 # Флаг проверки в случае сравнения с пользовательским файлом

# Проверка на сравнение с пользовательским файлом, его ввод и запись, либо запись из файла Scaned_Dir_File.txt

if not(s[-1] == '?'):
    fl = False # Флаг необходимости сравнения (повсеместно в коде)
else:
    fl = True
    file_to = input('Вы ввели "?" -> введите полный путь до файла для сравнения(с расширением): ')
    name = os.path.basename(file_to)
    file_to_open = file_to
    dir_to_scan = file_to.replace(name,'')
    fl2 = 1

if fl == False:
    for elem in os.listdir():
        if elem == 'Scaned_Dir_File.txt':
            name = 'Scaned_Dir_File.txt'
            fl = True

scaned_file_dir_un = []

# Запись файла сравнения

def ScanedFile(file_to_open):
    global scaned_file_dir_un
    with open(file_to_open, 'r') as f:
        for line in f:
            if line != '\n':
                if line != 'Список всех файлов и папок:\n':
                    scaned_file_dir_un.append(line.strip())
                else:
                    continue
            else:
                break
    print('Сравнение с данными из файла ' + file_to_open)

# Проверка правильности ввода пути пользователем

try:
    if fl == True:
        if fl2 == 1:
            os.chdir(dir_to_scan)
        ScanedFile(name)
except FileNotFoundError:
    print('Вы ввели неверное имя файла для сравнения, либо неверный путь к его директории.')
    exit(1)

try:
    if not(fl2 == 1):
        os.chdir(s)
    else:
        s = s[:len(s)-1]
        os.chdir(s)
except FileNotFoundError:
    print('Вы ввели неверный путь к директории.')
    exit(2)

path = os.path.abspath('.')

# Запись текущего состояния директории

file_dir_un = []
for elem in os.listdir():
    fullname = os.path.join(path, elem)
    if os.path.isfile(fullname):
        file_dir_un.append('File:      ' + str(fullname))
    elif os.path.isdir(fullname):
        file_dir_un.append('Directory: ' + str(fullname))
    else:
        file_dir_un.append('Unknown:   ' + str(fullname))

os.chdir(old_dir)

# Сравнения текущего и записанного состояний директории

def comparison(li, lj, fl):
    for i in range(len(li)):
        for j in range(len(lj)):
            if li[i] == lj[j]:
                flg = True
                break
            else:
                flg = False
        if flg == False:
            if fl == 2:
                diff_file_dir_un_add.append(li[i])
            elif fl == 1:
                diff_file_dir_un_del.append(li[i])
    c = li
    li = lj
    lj = c
    for i in range(len(li)):
        for j in range(len(lj)):
            if li[i] == lj[j]:
                flg = True
                break
            else:
                flg = False
        if flg == False:
            if fl != 2:
                diff_file_dir_un_add.append(li[i])
            elif fl != 1:
                diff_file_dir_un_del.append(li[i])
    return None

if fl == True:
    if len(scaned_file_dir_un) > len(file_dir_un):
        li = file_dir_un
        lj = scaned_file_dir_un
        flag = 1 # Флаг, чтобы наименования не повторялись
    elif len(scaned_file_dir_un) <= len(file_dir_un): 
        lj = file_dir_un
        li = scaned_file_dir_un
        flag = 2

diff_file_dir_un_add = []
diff_file_dir_un_del = []

if fl == True:
    comparison(lj, li, flag)

# Вывода в файл Scaned_Dir_File.txt

def DiffWriter(diff_list):
    f.write('Список всех ' + diff_action +'файлов и папок:' + '\n')
    for elem in diff_list:
        f.write(str(elem) + '\n')

with open('Scaned_Dir_File.txt', 'w') as f:
    diff_action = ''
    DiffWriter(file_dir_un)
    if fl == True and (diff_file_dir_un_add or diff_file_dir_un_del):
        if diff_file_dir_un_add:
            f.write('\n')
            diff_action = 'добавленных '
            DiffWriter(diff_file_dir_un_add)
        if diff_file_dir_un_del:
            f.write('\n')
            diff_action = 'удалённых '
            DiffWriter(diff_file_dir_un_del)

print('Текущее стостояние директории, а также итоги сравнения (если требовалось) представлены в файле "Scaned_Dir_File.txt".')