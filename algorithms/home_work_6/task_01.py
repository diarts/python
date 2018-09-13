# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.
# Python v3.6
# OS is Windows 10 x64

# Задача 1 из дз №5
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
#  для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
#  и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
# предприятий, чья прибыль ниже среднего.
# # Примечание: 4 квартала - это 4 разных прибыли ;-)
# Из задачи вычленен массив в котором будят храниться данные по компаниям и ввод осуществляется модулем random,
# так как нас в данный момент не интересует какую прибыль имели компании. Для примера компаний будет 4.
import random
import collections
import sys


def test_size(array, reqursion_level=1):
    global_size = sys.getsizeof(array)

    print('\t' * reqursion_level, f'Объект {array}')
    print('\t' * reqursion_level, f'типа {array.__class__}')
    print('\t' * reqursion_level, f'имеет размерность = {global_size}')

    if hasattr(array, '__iter__'):
        if array.__class__ == collections.OrderedDict or array.__class__ == dict:
            for value in array:
                global_size += test_size(value, reqursion_level + 1)
                global_size += test_size(array[value], reqursion_level + 2)

        elif not isinstance(array, str):
            for i in array:
                global_size += test_size(i, reqursion_level + 1)

    return global_size


# 1) сохранение данных по омпаниям в Dict
# Итог: размер класса Dict = 240 байт,
# размер словаря с 4 ключами компаний и их средней прибылью за 4 квартала = 583 байт
# Для решения данной задачи нам потребуется 2 дополнительных перебора всех переменных в словаре и
# сравнение их со средней стоимостью для вывода сначала копаний с прибылью больше средней, а затем с меньше средней.

COUNT_COMPANY = 4
QUARTES = 4
company_dict = {i: int(sum([random.randint(1000, 1000000) for _ in range(4)]) / QUARTES)
                for i in ('Coca Cola', 'Mac Donalds', 'Teremock', 'Crysler')}
print(f'Общий размер словаря company_dict = {test_size(company_dict)}')


# 2) сохранение данных по омпаниям в OrderedDict
# Итог: размер класса OrderedDict = 496 байт,
# размер словаря с 4 ключами компаний и их средней прибылью за 4 квартала = 839 байт
# Для решения данной задачи нам так же потребуется 2 дополнительных перебора всех переменных в словаре и
# сравнение их со средней стоимостью для вывода сначала копаний с прибылью больше средней, а затем с меньше средней.
COUNT_COMPANY = 4
QUARTES = 4
company_dict = {i: int(sum([random.randint(1000, 1000000) for _ in range(4)]) / QUARTES)
                for i in ('Coca Cola', 'Mac Donalds', 'Teremock', 'Crysler')}
company_dict = collections.OrderedDict(sorted(company_dict.items(), key=lambda x: x[1]))

print(f'Общий размер OrderedDict company_dict = {test_size(company_dict)}')


# 3) сохранение данных по омпаниям в множестве set
# Итог: размер класса set переменной all_company = 224 байт,
# внутри получается 4 объекта классна __main__.Company с размером 72 байта
# размер словаря с 4 ключами компаний и их прибылью за 4 квартала и средней прибылью = 1623 байта
# Для решения данной задачи нам все так же потребуется 2 дополнительных перебора всех переменных в множестве и
# сравнение их со средней стоимостью для вывода сначала сначала копаний с прибылью больше средней,
# а затем с меньше средней.

COUNT_COMPANY = 4
QUARTES = 4
Company = collections.namedtuple('Company', ['name', 'quartes', 'profit'])
all_company = set()

for i in ('Coca Cola', 'Mac Donalds', 'Teremock', 'Crysler'):
    quartes = []
    profit = 0

    for j in range(QUARTES):
        quartes.append(random.randint(1000, 1000000))
        profit += quartes[j]

    comp = Company(name=i, quartes = tuple(quartes), profit = profit)

    all_company.add(comp)

print(f'Общий размер множества all_company = {test_size(all_company)}')

Вывод: