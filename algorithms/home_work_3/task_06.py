# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Их самих в сумму не включать.
import random

MIN_RAND = -100
MAX_RAND = 100
LIST_RANGE = 10

my_list = [random.randint(MIN_RAND, MAX_RAND) for i in range(LIST_RANGE)]

find_min = my_list[0]
index_min = 0
find_max = my_list[0]
index_max = 0
total = 0

for index, value in enumerate(my_list):
    if value < find_min:
        find_min = value
        index_min = index
    elif value > find_max:
        find_max = value
        index_max = index

if index_min < index_max:
    for i in my_list[index_min + 1:index_max]:
        total += i
else:
    for i in my_list[index_max + 1:index_min]:
        total += i

print('В массисе:'
      f'\n{my_list}'
      f'\nминимальное значение = {find_min}, максимальное значение = {find_max}.'
      f'\nСумма чисел между ними = {total}')
