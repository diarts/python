# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
print('Добро пожаловать! Данная программа опреелит наибольшее по сумме цифр натурально число из введенных вами.')
max_value = 0
max_num = 0
num_list = []

while True:
    num = input('Введите число или \'stop\'(остановит подсчет): ')
    if num != 'stop':
        num_list.append(num)
    else:
        break

for count in num_list:
    value = 0
    for i in str(abs(int(count))):
        value += int(i)

    if max_value < value:
        max_value = value
        max_num = count

print(f'Среди введенных вами чисел\n{num_list} \nнаибольшее по сумме цифр число - {max_num}. \nСумма цифр этого числа = {max_value}')

