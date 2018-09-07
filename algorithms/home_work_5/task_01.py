# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
#  для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
#  и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
# предприятий, чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

import collections
import random

# count_company = int(input('Введите количество компаний: '))
count_company = 4

# company_dict = {input(f'Введите название {i} компании: '):
#                     sum([float(input(f'Введите прибыль компании {i} для {j} квартала: ')) for j in range(1, 5)])/4
#                 for i in range(1, count_company + 1)}
#
company_dict = {input(f'Введите название {i} компании: '):
                    sum([float(random.randint(5, 10000000)) for j in range(1, 5)]) / 4
                for i in range(1, count_company + 1)}
company_dict = collections.OrderedDict(sorted(company_dict.items(), key=lambda x: x[1]))

middle = 0
for value, item in enumerate(company_dict):
    middle += company_dict[item]
middle /= len(company_dict)
print(middle)
print(company_dict)

print('Компании, чья прибыль ниже средней(для всех предприятий) за год: ', end='')
print(*list(item for value, item in enumerate(company_dict) if value < middle), sep=', ')

print('Компании, чья прибыль ниже средней(для всех предприятий) за год: ', end='')
print(list(item for value, item in enumerate(company_dict) if value > middle))
