# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import cProfile
#  №1 Решето Эратосфена





# №2 Свой вариант

def find_simple_num(index):
    num = 3
    simple_nums = [2]
    nums = [2]
    while True:
        if len(simple_nums) == index:
            print(f'Ваше {index} простое число = {simple_nums[index-1]}')
            break
        else:
            for i in nums:
                if num % i == 0:
                    nums.append(num)
                    break
            else:
                nums.append(num)
                simple_nums.append(num)
        num += 1

# timeit find_simple_num(100):
# 100 loops, best of 3: 1.48 msec per loop

# timeit find_simple_num(500):
# 100 loops, best of 3: 47.6 msec per loop


# cProfile.run('find_simple_num(100)')
# 1    0.002    0.002    0.002    0.002 task_02.py:12(find_simple_num)

# cProfile.run('find_simple_num(500)')
# 1    0.049    0.049    0.050    0.050 task_02.py:12(find_simple_num)

# cProfile.run('find_simple_num(1000)')
# 1    0.288    0.288    0.289    0.289 task_02.py:12(find_simple_num)

# cProfile.run('find_simple_num(2000)')
# 1    1.034    1.034    1.037    1.037 task_02.py:12(find_simple_num)