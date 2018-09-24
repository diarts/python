# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N. Например,
#  состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке. Для
# решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

import hashlib
import collections


def hash_count(your_word):
    '''
    Функция принимает любую строку
    :param your_word: принимаемая строка
    :return: возвращает OrderedDict с ключами - подстроками и значениями - хешами этих подстрок
    '''
    word = str(your_word)

    word_hash = hashlib.sha1(bytes(word, 'utf-8')).hexdigest()

    hash_list = {}
    collections.OrderedDict(hash_list)

    for i in range(len(word)):
        letter = ''
        for j in word[i:]:
            letter += j
            hash_letter = hashlib.sha1(bytes(letter, 'utf-8')).hexdigest()

            if hash_letter != word_hash and hash_letter not in hash_list:
                hash_list[letter] = hash_letter

    return hash_list


while True:
    my_word = input('Введите строку, количество хешированных подстрок которой вы хотите найти: ')
    if my_word == '':
        print('Вы ничего не ввели, попробуйте еще раз!')
    else:
        break

my_word_hash = hash_count(my_word)
print(f'\nВ вашей строке {my_word} содержится {len(my_word_hash)} хешированных подстрок:')

for key, value in my_word_hash.items():
    print('\t', f'{key} - {value}')
