# 2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.
import collections


class MyUntil():
    def __init__(self, value, left=None, right=None, letter=None):
        self.value = value
        self.left = left
        self.right = right
        self.letter = letter

    def print_until(self, tab=1):
        ''' Печать дерева со всеми его узлами и листьями по принципу вложения'''
        requrs_tabulation = tab * 2

        print(f'(value = {self.value}, letter = {self.letter}')
        if self.left != None:
            print('\t' * requrs_tabulation, 'left = ', end='')
            self.left.print_until(1 + tab)
        else:
            print('\t' * requrs_tabulation, f'left = None')

        if self.right != None:
            print('\t' * requrs_tabulation, 'right = ', end='')
            self.right.print_until(1 + tab)
        else:
            print('\t' * requrs_tabulation, f'right = None)')

    def __repr__(self):
        ''' Отображение класса при вызове функцией print'''
        return f'(value = {self.value}, letter = {self.letter}, left = {self.left}, right = {self.right})'


def get_value(myuntil):
    return myuntil.value


def create_foliage(word):
    '''
    Функция создания списка состоящего из листьев дерева
    :param word: список формата counter модуля collection, объекты которого нужно превратить в листья
    :return:отсортированыый по параметру value список листьев дерева
    '''

    foliage = []

    for value in word:
        letter = MyUntil(word[value], letter=value)
        foliage.append(letter)

    foliage.sort(key=get_value)
    return foliage


def until_create(sheet_1, sheet_2):
    '''
    Функция сбора из двух листов узла
    :param sheet_1: лист 1, имеет меньший вес
    :param sheet_2: лист 2, имеет больший или равный листу 1 вес
    :return: узел с двумя листьями
    '''
    tree = MyUntil(sheet_1.value + sheet_2.value, left=sheet_1, right=sheet_2, letter=None)
    return tree


def set_tree(foliage_list, tree):
    '''
    Функция вставки дерева в массив листьев по значению его value так, чтобы дерево было первим среди всех
    объектов словаря со схожим параметром value
    :param foliage_list: массив листьев
    :param tree: дерево
    :return: массив листьев с вставленным в него деревом
    '''
    for index, sheet in enumerate(foliage_list):
        if sheet.value == tree.value:
            foliage_list.insert(index, tree)
            return foliage_list
        elif sheet.value < tree.value and index == len(foliage_list) - 1:
            foliage_list.append(tree)
            return foliage_list
        elif sheet.value < tree.value and foliage_list[index + 1].value > tree.value:
            foliage_list.insert(index + 1, tree)
            return foliage_list


def tree_create(foliage):
    '''
    Функция сбора дерева из листьев
    :param foliage: массив листьев
    :return: массив только с 1 объектом - собраным деревом
    '''
    while len(foliage) == 2:
        tree = until_create(foliage[0], foliage[1])
        return tree
    else:
        tree = MyUntil(foliage[0].value + foliage[1].value, left=foliage.pop(0), right=foliage.pop(0), letter=None)
        set_tree(foliage, tree)
        return tree_create(foliage)


def find_letter_in_tree(tree, find_letter, stack):
    '''
    Получение пути в дереве до заданой буквы
    :param tree: дерево
    :param find_letter: буква, котору ищем
    :param stack: путь, по которому нашли букву
    :return: путь по которому была найдена буква
    '''
    if tree.letter == None:
        if find_letter_in_tree(tree.left, find_letter, stack) != None:
            stack.appendleft(0)
            return stack
        elif find_letter_in_tree(tree.right, find_letter, stack) != None:
            stack.appendleft(1)
            return stack
        else:
            return None
    else:
        if find_letter == tree.letter:
            return True
        else:
            return None


def convert_deque_to_str(deque):
    '''
    Конверитрование из типа collection deque в тип string
    :param deque: заданая очередь
    :return: строка
    '''
    c_string = ''
    for i in deque:
        c_string += str(i)
    return c_string


def create_encoding_table(word, tree):
    '''
    Создание таблицы кодировки для букв в заданом слове на основе ее нахождения в дереве
    :param word: Слово, на основе которого строится таблица кодировки
    :return: Готовая таблица кодировки
    '''
    encoding_table = {}
    for i in word:
        if i not in encoding_table:
            stack = collections.deque([])
            encoding_table[i] = convert_deque_to_str(find_letter_in_tree(tree, i, stack))

    return encoding_table


def create_haffman_coding(word, encoding_table):
    '''Перевод текста в кодировку'''
    coding_word = ''
    for i in word:
        coding_word += encoding_table[i]
    return coding_word


def haffman_encoding(word):
    '''Функция архивирования и кодирования заданного текста по методу Хаффмана'''
    word_collections = collections.Counter(word)
    foliage = create_foliage(word_collections)
    tree = tree_create(foliage)
    tree.print_until()
    encoding_table = create_encoding_table(word, tree)
    coding_word = create_haffman_coding(word, encoding_table)
    return coding_word, encoding_table


while True:
    word = input('Введите текст, который хотите заархивировать: ')
    if word == '':
        print('Вы ничего не ввели, попробуйе еще раз!')
    else:
        break

coding_word, encoding_table = haffman_encoding(word)
print(f'Ваш текст {word} в заархивированном виде выглядит следующим образом: \n{coding_word}\nтаблица кодировки '
      f'= {encoding_table},\n')
