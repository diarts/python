# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

def merge_sort(list):

    if len(list) == 1:
        return list

    final_list = []
    new_list_1 = merge_sort(list[0: len(list) // 2])
    new_list_2 = merge_sort(list[len(list) // 2: len(list) + 1])
    IND = 0

    while len(new_list_1) > 0 and len(new_list_2) > 0:

            if new_list_1[IND]< new_list_2[IND]:
                final_list.append(new_list_1.pop(IND))
            else:
                final_list.append(new_list_2.pop(IND))

    if len(new_list_1) == 0:
        final_list += new_list_2
    else:
        final_list += new_list_1

    return final_list


try:
    len_array = int(input('Введите длину массива: '))
except ValueError:
    print('Вы ввели не число, длина может быть указана только числом!')
else:
    if len_array == 0:
        print('Длина массива не может быть = 0!')
    elif len_array < 0:
        print('Длина массива не может быть отрицательной!')
    else:
        my_list = [random.randint(0, 50) for i in range(len_array)]
        print(f'Рандомно созданный массив длиной {len_array}: \n{my_list}\n')
        print(f'Отсортированый массив: \n{merge_sort(my_list)}')