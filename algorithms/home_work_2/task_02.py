# Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
even = 0
odd = 0
even_list = []
odd_list = []

count = input('Введите натуральное число, четные и нечетные числа которого хотите найти: ')
count_for = count

if int(count) < 0:
    count_for = count[1:]

for i in count_for:
    if int(i) % 2 == 0:
        even += 1
        even_list.append(i)
    else:
        odd += 1
        odd_list.append(i)

print(f'\nУ введенного числа {count} есть {even} четных цифр {even_list} и {odd} нечетных цифр {odd_list}.')
