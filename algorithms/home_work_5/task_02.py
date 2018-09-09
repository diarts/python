# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# A = 10, B=11, C=12, D=13, E=14, F=15
import collections


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


def alignment(deque):
    deque = collections.deque(deque)
    deque.reverse()
    value = 0

    for index, num in enumerate(deque):
        num += value
        if num < 16:
            deque[index] = num
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
    elif value !=0:
        deque.append(value)

    deque.reverse()
    return deque


def num_multi(num_1, num_2):
    num_1 = collections.deque(num_1)
    num_2 = collections.deque(num_2)
    multy_line = collections.deque()
    if len(num_2) > len(num_1):
        finish_line = [0]*len(num_2)
    else:
        finish_line = [0]*len(num_1)
    finish_line = collections.deque(finish_line)

    num_1.reverse()
    num_2.reverse()


    for factor_1 in num_1:
        for factor_2 in num_2:
            multy_line.append(int(factor_1) * int(factor_2))

        finish_line = num_summ(multy_line, finish_line)

    finish_line.reverse()
    return finish_line



num_1 = collections.deque(input('Введите первое шестнадцатеричное число: ').upper())
num_2 = collections.deque(input('Введите второе шестнадцатеричное число: ').upper())

num_converter(True, num_1, num_2)

deque_multy = num_multi(num_1, num_2)

print('multi', deque_multy)

deque_multy = alignment(deque_multy)

print('alignment', deque_multy)

deque_multy = num_converter(False, deque_multy)

print(deque_multy)



# deque_summ = num_summ(num_1.copy(), num_2.copy())
#
# deque_summ = alignment(deque_summ)
#
# num_converter(False, deque_summ)
# print(deque_summ, '\n')


