# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из
# чисел в диапазоне от 2 до 9.
multiple = [0] * 8

for i in range(2, 100):
    if i % 2 == 0:
        multiple[0]+=1
    if i%3 == 0:
        multiple[1]+=1
    if i%4 == 0:
        multiple[2]+=1
    if i % 5 == 0:
        multiple[3] += 1
    if i % 6 == 0:
        multiple[4] += 1
    if i % 7 == 0:
        multiple[5] += 1
    if i % 8 == 0:
        multiple[6] += 1
    if i % 9 == 0:
        multiple[7] += 1

print('В диапазоне натуральных чисел от 2 до 99:\n'
      f'{multiple[0]} чисел кратных 2\n'
      f'{multiple[1]} числа кратных 3\n'
      f'{multiple[2]} числа кратных 4\n'
      f'{multiple[3]} чисел кратных 5\n'
      f'{multiple[4]} чисел кратных 6\n'
      f'{multiple[5]} чисел кратных 7\n'
      f'{multiple[6]} чисел кратных 8\n'
      f'{multiple[7]} чисел кратных 9')