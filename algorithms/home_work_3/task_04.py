# Определить, какое число в массиве встречается чаще всего.
import random

my_list = [random.randint(0, 10) for _ in range(10)]
waste_num = []
counter = 0
final_counter = 0
final_num = 0

for num in my_list:
    if num not in waste_num:
        waste_num.append(num)
        for i in my_list:
            if num == i:
                counter += 1
        if counter > final_counter:
            final_counter = counter
            final_num = num
        counter = 0

print('В массиве '
      f'\n{my_list}'
      f'\n число {final_num} встречается чаще остальных, а именно {final_counter} раз')
