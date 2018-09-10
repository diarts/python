# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# A = 10, B=11, C=12, D=13, E=14, F=15
import collections
import re


def num_converter(in_nums=True, *args):
    un_reverce_converter_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    reverce_convert_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if in_nums == True:
        converter_dict = un_reverce_converter_dict
    else:
        converter_dict = reverce_convert_dict

    for list in args:
        for index, num in enumerate(list):
            if num in converter_dict:
                list[index] = converter_dict[num]


'''Function converted hexadecimal symbol (A, B, C, D, E, F) in nums (11, 12, 13, 14, 15) and back.
in_nums = True (default) if you need convert from symbol to nums
in_nums = False if you need convert from nums to symbol'''


def num_summ(num_1, num_2):
    if len(num_1) < len(num_2):
        num_1, num_2 = num_2, num_1
    deque_summ = collections.deque()

    for _ in range(len(num_2)):
        num = int(num_1.pop()) + int(num_2.pop())
        deque_summ.appendleft(num)

    for _ in range(len(num_1)):
        num = int(num_1.pop())
        deque_summ.appendleft(num)
    return deque_summ


def num_multi(num_1, num_2):
    num_1 = collections.deque(num_1)
    num_2 = collections.deque(num_2)
    multy_line = collections.deque()

    if len(num_2) > len(num_1):
        finish_line = collections.deque([0] * len(num_2))
    else:
        finish_line = collections.deque([0] * len(num_1))

    num_1.reverse()
    num_2.reverse()

    for index, factor_1 in enumerate(num_1):
        for factor_2 in num_2:
            multy_line.appendleft(int(factor_1) * int(factor_2))

        for _ in range(index):
            multy_line.append(0)

        finish_line = num_summ(multy_line, finish_line)

    return finish_line


def alignment(deque):
    deque = collections.deque(deque)
    deque.reverse()
    value = 0

    for index, num in enumerate(deque):
        num += value
        if num < 16:
            deque[index] = num
            value = 0
        else:
            rest = num % 16
            value = num // 16
            deque[index] = rest

    if value != 0 and value > 16:
        while True:
            rest = value % 16
            value = value // 16
            deque[-1] = rest
            deque.append(value)
            if value < 16:
                break
    elif value != 0:
        deque.append(value)

    deque.reverse()
    return deque


def hexadecimal_sum(num_1, num_2):
    num_converter(True, num_1, num_2)
    deque_summ = num_summ(num_1.copy(), num_2.copy())
    deque_summ = alignment(deque_summ)
    num_converter(False, deque_summ)
    return deque_summ


def hexadecimal_multiplication(num_1, num_2):
    num_converter(True, num_1, num_2)
    deque_multy = num_multi(num_2, num_1)
    deque_multy = alignment(deque_multy)
    num_converter(False, deque_multy)
    return deque_multy


def input_num():
    re_string = '^[0-9ABCDEF]+$'
    while True:
        input_1 = input('Введите первое шестнадцатеричное число: ').upper()
        if re.match(re_string, input_1) == None:
            print('Вы ввели не шестнадцатеричное число, попробуйте еще раз!')
        else:
            input_1 = collections.deque(input_1)
            break

    while True:
        input_2 = input('Введите второе шестнадцатеричное число: ').upper()
        if re.match(re_string, input_2) == None:
            print('Вы ввели не шестнадцатеричное число, попробуйте еще раз!')
        else:
            input_2 = collections.deque(input_2)
            break
    return input_1, input_2


def print_hexadecimal(num_1, num_2, answer, type_print='Сумма'):
    print(f'{type_print} двух шестнадцатеричных чисел ', end='')
    print(*num_1, ' и ', *num_2, ' = ', *answer, '\n\n', sep='', end='')


print('Добро пожаловать в программу сложения и умножения шестнадцатеричных чисел.\n')

while True:
    print('Выберите из списка, что вы хотете сделать:\n'
          '1. Сложить два шестнадцатеричных числа\n'
          '2. Перемножить два шестнадцатеричных числа\n'
          '3. Выйти из программы\n')
    try:
        change = int(input('Введите номер действия, которое вы хотите сделать: '))

    except ValueError:
        print('Вы ввели не число. Нужно ввести номер действия которое вы хотите сделать числом! Попробуйте еще раз.\n')

    else:
        if change not in {1, 2, 3}:
            print(f'В программе нет действия с номером {change}. Попробуйте еще раз.')
        elif change == 3:
            break
        elif change == 1:
            num_1, num_2 = input_num()
            answer = hexadecimal_sum(num_1.copy(), num_2.copy())
            print_hexadecimal(num_1, num_2, answer)
        else:
            num_1, num_2 = input_num()
            answer = hexadecimal_multiplication(num_1.copy(), num_2.copy())
            print_hexadecimal(num_1, num_2, answer, 'Произведение')
