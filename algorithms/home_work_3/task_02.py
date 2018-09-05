# Во втором массиве сохранить индексы четных элементов первого массива. Например, если
# дан массив со значениями 8, 3, 15, 6, 4, 2, то второй массив надо заполнить значениями 1, 4,
# 5, 6 (или 0, 3, 4, 5 – если индексация начинается с нуля), так как именно в этих позициях
# первого массива стоят четные числа.
import random

MAX_LIST_NUM = 1000
MIN_LIST_NUM = 0
MAX_LEN_LIST = 100
MIN_LIST_LEN = 1

nums_list = [random.randint(MIN_LIST_NUM, MAX_LIST_NUM) for _ in range(random.randint(MIN_LIST_LEN, MAX_LEN_LIST))]
even_list = []

for index, value in enumerate(nums_list):
    if value % 2 == 0:
        even_list.append(index)

print(f'В массиве \n{nums_list} \nчетные элементы находятся на индексах: \n{even_list}')
