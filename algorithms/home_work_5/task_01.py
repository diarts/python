# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
#  для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
#  и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
# предприятий, чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

import collections

count_company = int(input('Введите количество компаний: '))

company_dict = {input(f'Введите название {i} компании: '):
                    int(sum([int(input(f'Введите прибыль компании {i} для {j} квартала: ')) for j in range(1, 5)])/4)
                for i in range(1, count_company + 1)}
company_dict = collections.OrderedDict(sorted(company_dict.items(), key=lambda x: x[1]))

middle = 0
for company_name in company_dict:
    middle += company_dict[company_name]
middle = int(middle/len(company_dict))

print(f'\n\nВсе компани и их средняя прибыль за год: ')
print(*list(f'{company_name}: {company_dict[company_name]}$, ' for company_name in company_dict))
print(f'Средняя прибыль среди всех компаний за год = {middle}$')

print('\nКомпании, чья прибыль больше средней(для всех предприятий) за год: ', end='')
print(*list(f'{company_name}: {company_dict[company_name]}$'
            for company_name in company_dict if company_dict[company_name] > middle), sep=', ')

print('\nКомпании, чья прибыль ниже средней(для всех предприятий) за год: ', end='')
print(*list(f'{company_name}: {company_dict[company_name]}$'
            for company_name in company_dict if company_dict[company_name] < middle), sep=', ')

