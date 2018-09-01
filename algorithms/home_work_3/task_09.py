# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

MATRIX_RAW = int(input('Введите сколько должно быть у матрицы строк: '))
MATRIX_COLL = int(input('Введите сколько должно быть у матрицы столбцов: '))
MATRIX_RAND_MIN = int(input('Введите минимальную границу для чисел, которыми будет заполнена матрица: '))
MATRIX_RAND_MAX = int(input('Введите максимальную границу для чисел, которыми будет заполнена матрица: '))

matrix = [[random.randint(MATRIX_RAND_MIN, MATRIX_RAND_MAX) for collumn in
           range(1, MATRIX_COLL + 1)] for raw in range(1, MATRIX_RAW + 1)]

matrix_min_list = [MATRIX_RAND_MAX] * MATRIX_COLL
max_element = MATRIX_RAND_MIN

for row in range(MATRIX_RAW):
    for coll in range(MATRIX_COLL):
        if matrix[row][coll] < matrix_min_list[coll]:
            matrix_min_list[coll] = matrix[row][coll]

for element in matrix_min_list:
    if element > max_element:
        max_element = element

print('В рандомнозаданной матрице:')
for raw in range(MATRIX_RAW):
    print(matrix[raw])

print('минимальные значение столбцов:'
      f'\n{matrix_min_list}'
      f'\nсамое большое из которых = {max_element}')
