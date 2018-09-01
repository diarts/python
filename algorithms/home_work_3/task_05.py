# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию в массиве.

import random

MIN_RAND = -100
MAX_RAND = 100
LIST_RANGE = 10

my_list = [random.randint(MIN_RAND, MAX_RAND) for i in range(LIST_RANGE)]
find_num = MIN_RAND
find_index = 0
count_pos_num = 0

for index, num in enumerate(my_list):
    if num < 0:
        if num > find_num:
            find_num = num
            find_index = index
    else:
        count_pos_num += 1

if count_pos_num == len(my_list):
    print('В массиве:'
          f'\n{my_list}'
          '\nтолько положительные числа')
else:
    print('Максимальный отрицательный элемент массива'
          f'\n{my_list}'
          f'\n это число {find_num}, его позиция в массиве = {find_index}')
