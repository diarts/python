# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа
# должна не завершаться, а запрашивать новые данные для вычислений. Завершение
# программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа сообщает ему об ошибке
# и снова запрашивает знак операции. Также пользователю нужно сообщать о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.

while True:
    print ('Добро пожаловать в калькулятор!\n'
           'Для выбора действия укажите его символ:\n'
           '+ Для сложения\n'
           '- Для вычитания\n'
           '* для умножения\n'
           '/ для деления\n')
    choosen = input('Введите символ требуемого действия: ')

    if choosen == '+':
        count_1 = input('Введите первое число которое хотите сложить: ')
        count_2 = input('Введите первое число которое хотите сложить: ')