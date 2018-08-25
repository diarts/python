# Пользователь вводит две буквы. Определить их порядковый номер в алфавите и рассчитать
# число букв между ними.

alphabet = (
    '', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z')

if __name__ == '__main__':

    sym_1 = input('Введите первый символ от a до z:  ')
    sym_2 = input('Введите второй символ от a до z:  ')

    sym_1 = sym_1.lower()
    sym_2 = sym_2.lower()

    print(f'Порядковый номер символа {sym_1} в алфавите = {alphabet.index(sym_1)}')
    print(f'Порядковый номер символа {sym_2} в алфавите = {alphabet.index(sym_2)}')

    if alphabet.index(sym_2) > alphabet.index(sym_1):
        print(
            f'Между символами {sym_1} и {sym_2} находится {alphabet.index(sym_2)-alphabet.index(sym_1) -1} символов')
    else:
        print(
            f'Между символами {sym_1} и {sym_2} находится {alphabet.index(sym_1)-alphabet.index(sym_2) -1} символов')
