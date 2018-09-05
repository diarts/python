# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.
import random

MAX_NUMS_LIST = 1000
MIN_NUMS_LIST = 1
LEN_LIST = 10

nums_list = [random.randint(MIN_NUMS_LIST, MAX_NUMS_LIST) for _ in range(LEN_LIST)]

index_max_num = 0
index_min_num = 0
value_max_num = nums_list[0]
value_min_num = nums_list[0]

for index, value in enumerate(nums_list):
    if value > value_max_num:
        value_max_num = value
        index_max_num = index

    if value < value_min_num:
        value_min_num = value
        index_min_num = index

print(f'В заданном списке: \n{nums_list} \nпоменяли местами максимальное({value_max_num}) и '
      f'минимальное({value_min_num}) значение. Получился список:')
nums_list[index_min_num], nums_list[index_max_num] = nums_list[index_max_num], nums_list[index_min_num]
print(nums_list)
