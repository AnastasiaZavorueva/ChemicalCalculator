import re

from config import keys

vvod = input('Введите формулу вещества: ')

substance = re.sub('(?<=\d)(?!\d)|(?<!\d)(?=\d)', ' ', vvod)
list_elements = substance.split()
elements = ' '.join(list_elements)

list_numbers = []
num = ''
for char in elements:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            list_numbers.append(int(num))
            num = ''
if num != '':
    list_numbers.append(int(num))

string_numbers = [str(item) for item in list_numbers]

list_letters = list_elements+string_numbers
string_elements = []
for i in list_letters:
    if i not in string_elements:
        string_elements.append(i)
    else:
        string_elements.remove(i)

len = len(string_elements)
num = 0
mass = 0
while num < len:
    mass = mass + float(keys[string_elements[num]]) * float(list_numbers[num])
    num += 1

print('Молекулярная масса вещества равна', mass, 'г/моль')