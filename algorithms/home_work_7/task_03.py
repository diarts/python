# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.
import random


def get_median(list):
    for index, num in enumerate(list):
        bigger = 0
        small = 0
        equal = -1

        for i in list:
            if num > i:
                small += 1
            elif num < i:
                bigger += 1
            else:
                equal += 1

        if (bigger == len(list) // 2 and small == len(list) // 2) or \
                (equal > 0 and (bigger + equal == small or small + equal == bigger)): return num, index

MIN_RAND = 0
MAX_RAND = 100
HALF_OF_LEN = 10

my_list = [random.randint(MIN_RAND, MAX_RAND) for _ in range(2*HALF_OF_LEN+1)]
median, arr_index = get_median(my_list)

print(f'Для случайно заданого массива: \n{my_list} \nмедианой является число {median}, которое стоит в массиве '
      f'по порядку под номером {arr_index + 1}\n')

# Для проверки правильности нахождения медианы отсотрируем массив
my_list.sort()
print('Для проверки возьмем отсортированный массив my_list: \n', my_list, sep='')
print('чтобы получить его медиану, нам нужно разделить его длину целочислено на 2, полученное число будет индекс '
      f'медианы в массиве, \nузнав его мы получаем саму медиану: {my_list[len(my_list)//2]}')

