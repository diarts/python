# Определить, является введённый пользователем год високосным или нет.

year = int(input('Введите год в числовом формате, который хотите проверить: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'Год {year} високосный')
        else:
            print(f'Год {year} не является високосным')
    else:
        print(f'Год {year} високосный')
else:
    print(f'Год {year} не является високосным')
