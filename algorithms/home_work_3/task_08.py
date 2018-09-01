# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в
# последнюю ячейку строки. В конце следует вывести полученную матрицу.
import random
matrix = [[int(input(f'Введите число для стобца {collumn}, '
                 f'строки {raw} в матрице: ')) for collumn in range(1, 5)] for raw in range(1, 5)]
# matrix = [[random.randint(0, 100) for collumn in range(1, 5)] for raw in range(1, 5)]

print('Ваша матрица:'
      f'\n{matrix[0]}'
      f'\n{matrix[1]}'
      f'\n{matrix[2]}'
      f'\n{matrix[3]}')

for index in range(4):
    matrix[index].append(sum(matrix[index]))

print('\nМатрица после добавления суммы всех элементов в последнюю ячейку строки:'
      f'\n{matrix[0]}'
      f'\n{matrix[1]}'
      f'\n{matrix[2]}'
      f'\n{matrix[3]}')