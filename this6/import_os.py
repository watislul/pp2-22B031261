import os
#1
'''
path = os.getcwd()
dirs = os.listdir(path)
for index in dirs:
    if os.path.isdir(index):
        print(f'DIR => {index}')
    elif os.path.isfile(index):
        print(f'FILE => {index}')
'''
#2
'''
path = input()

try:
    os.chdir(path)
    print(os.access(path, os.W_OK))
except Exception as e:
    print(e)
'''
#3
'''
path = input() # введите путь до папки в которой находится файл

try:
    os.chdir(path)
    txt = input() # введите название файла с его расширением
    output = open(txt, 'r')
    output = output.read().split('\n')

    print(f'Количество строк: {len(output)}')
except Exception as e:
    print(e)
'''
#4


#5
'''
path = input()

try:
     os.chdir(path)
     for index in range(65, 91):
         output = open(chr(index)+'.txt', 'w')
except Exception as e:
    print(e)
'''
#7
path = input()
try:
    os.chdir(path)
    txt1 = input()
    path2 = input()
    txt2 = input()
    with open(txt1,'r') as input, open(path + '/' + txt2, 'a') as output:
        for line in input:
            output.write(line)
except Exception as e:
    print(e)
#8

print('Укажите путь: ')
path = input()

try:
    os.chdir(path)
    dirs = os.listdir(os.getcwd())
    print('Выберите папку или файл для удаления: ')
    for i in dirs:
        if os.path.isdir(i):
            print(f'<DIR> {i}')
        elif os.path.isfile(i):
            print(f'<FILE> {i}')
    print('Введите имя файла:')
    name = input()
    if os.access(f'./{name}', os.W_OK):
        os.remove(name)
    else:
        print('Нет доступа к этому файлу')

except Exception as e:
    print(e)