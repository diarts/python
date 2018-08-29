# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
# экран. Например, если введено число 3486, то надо вывести 6843.

def compulation(count):
    if count // 10 != 0:
        value = count % 10
        count = int(count / 10)
        return (value + compulation(count)) / 10
    else:
        return count / 10


orig_count = int(input('Введите любое целочисленое число, которое хотите отразить: '))

for i in range(1, abs(orig_count)):
    if abs(orig_count) // (10 ** i) == 0:
        dozen = i
        break

find_count = compulation(abs(orig_count))

if orig_count < 0:
    find_count *= -1

print(f'Отражением вашего числа {orig_count} является число {int(find_count*(10**dozen))}')
