# Найти сумму и произведение цифр введённого пользователем трехзначного числа.

num = input("Введите любое трёхзначное число: ")

if len(num) == 3:
    num_1 = int(num[0])
    num_2 = int(num[1])
    num_3 = int(num[2])
else:
    num_1 = int(num[:2])
    num_2 = int(num[2])
    num_3 = int(num[3])

print(f'Сумма цифр трехзначного числа {num} = {num_1 + num_2 + num_3}')
print(f'Произведение цифр трехзначного числа {num} = {num_1 * num_2 * num_3}')
