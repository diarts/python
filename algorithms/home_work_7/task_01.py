# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
import random


def my_buble_sort(list, first_be='max'):
    '''
    Сортировка пузырьком, немного ускоренная.
    :param list: Массив который требуется отсортировать
    :param first_be: параметр по дефолту = max, max - это значит сортировать по убыванию, min - сотрировать по возрастанию
    :return: отсортированый массив и количество циклов затраченных на сортировку
    '''
    n = 0
    for i in range(len(my_list)):
        for j in range(0 + i, len(my_list)):

            if first_be == 'max':
                if my_list[i] < my_list[j]:
                    my_list[i], my_list[j] = my_list[j], my_list[i]
            elif first_be == 'min':
                if my_list[i] > my_list[j]:
                    my_list[i], my_list[j] = my_list[j], my_list[i]
            n += 1
    return my_list, n


def buble_sort(list, first_be='max'):
    n = 0
    for _ in range(len(my_list)):
        for j in range(len(my_list) - 1):

            if first_be == 'max':
                if my_list[j] < my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            elif first_be == 'min':
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            n += 1
    return my_list, n


my_list = [random.randint(-100, 100) for _ in range(20)]
print(f'Заданный массив:\n{my_list}')

my_buble_list, my_buble_count = my_buble_sort(my_list)
print(f'\nОтсортированный массив с помощью ускореной функции \n{my_buble_list},\n сортировка осуществлена за '
      f'{my_buble_count} циклов')

# Сравнение с стандартной функцией, показаной на уроке
classic_buble_list, classic_buble_count = buble_sort(my_list)
print(f'\nОтсортированный массив с помощью стандартной функции \n{classic_buble_list},\n сортировка осуществлена за '
      f'{classic_buble_count} циклов')