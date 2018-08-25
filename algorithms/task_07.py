# По введенным пользователем длинам трех отрезков определить, можно ли составить из этих
# отрезков треугольник. Если да, определить, будет ли треугольник равносторонним,
# равнобедренным или равносторонним.

section_1 = int(input('Введите длину первого отрезка(числа должны быть целыми): '))
section_2 = int(input('Введите длину второго отрезка(числа должны быть целыми): '))
section_3 = int(input('Введите длину третьего отрезка(числа должны быть целыми): '))

if section_1 + section_2 > section_3 and section_2 + section_3 > section_1 and section_3 + section_1 > section_2:
    if section_1 == section_2 == section_3:
        print(f'Из отрезков {section_1}, {section_2} и {section_3} можно построить равносторонний треугольник')
    else:
        if section_1 == section_2 or section_2 == section_3 or section_1 == section_3:
            print(f'Из отрезков {section_1}, {section_2} и {section_3} можно построить равнобедренный треугольник')
        else:
            print(f'Из отрезков {section_1}, {section_2} и {section_3} можно построить только обычный треугольник')
else:
    print(f'Из отрезков {section_1}, {section_2} и {section_3} нельзя построить треугольник')
