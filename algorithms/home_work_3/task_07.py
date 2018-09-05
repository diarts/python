# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.
import random

MIN_RAND = -100
MAX_RAND = 100
LIST_RANGE = 10

my_list = [random.randint(MIN_RAND, MAX_RAND) for i in range(LIST_RANGE)]

first_min_num = my_list[0]
second_min_num = my_list[0]

for i in my_list:
    if i < first_min_num:
        second_min_num = first_min_num
        first_min_num = i
    elif i == first_min_num or (i > first_min_num and i < second_min_num):
        second_min_num = i

print('В массиве чисел:'
      f'\n{my_list}'
      f'\nсамое маленькое число = {first_min_num},  '
      f'\nвторое самое маленькое число = {second_min_num}')
