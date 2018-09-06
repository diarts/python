# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import cProfile
#  №1 Решето Эратосфена
def eratosfen(index):
    if index<600:
        LAST_INDEX = (index // 20)*150
    elif index<600000:
        LAST_INDEX = (index // 20) * 300
    else:
        LAST_INDEX = (index // 20) * 500

    sieve = [i for i in range(LAST_INDEX)]

    sieve[1] = 0

    for i in range(2, LAST_INDEX):
        if sieve[i] != 0:
            j = i * 2
            while j < LAST_INDEX:
                sieve[j] = 0
                j += i

    sieve_simple_num = [i for i in sieve if i != 0]
    print(sieve_simple_num[index-1])

# timeit find_simple_num(100):
# 100 loops, best of 3: 393 usec per loop

# timeit find_simple_num(500):
# 100 loops, best of 3: 1.5 msec per loop

# timeit find_simple_num(1000):
# 100 loops, best of 3: 5.89 msec per loop

# cProfile.run('eratosfen(100)')
# 1    0.000    0.000    0.000    0.000 task_02.py:5(eratosfen)

# cProfile.run('eratosfen(500)')
# 1    0.001    0.001    0.001    0.001 task_02.py:5(eratosfen)

# cProfile.run('eratosfen(1000)')
# 1    0.004    0.004    0.005    0.005 task_02.py:5(eratosfen)

# cProfile.run('eratosfen(700000)')
# 1    7.994    7.994   10.181   10.181 task_02.py:5(eratosfen)

# Итог: Решето все еще лучши вариант

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