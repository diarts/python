# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
# заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар
# «код-символ» в каждой строке.
print('\nТАБЛИЦА С СИМВОЛАМИ ТАБЛИЦЫ ASCII C 32 ПО 127\n')

letter = 31

for _ in range(1, 11):
    for _ in range(1, 11):
        if letter == 127:
            break
        else:
            letter += 1
            print(f' {letter} - \'{chr(letter)}\' |', end='')
    else:
        print('\n')
