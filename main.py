from typing import Callable, Any, Union
from random import randint as rint


class Iterator:
    def __init__(self,
                 iter_object: Union[list, tuple, ...],
                 key: Callable = None,
                 reverse: bool = False):

        self.iter_object = list(iter_object)
        self.key = key
        self.reverse = reverse
        self.index = 0

    def __next__(self):
        if self.index >= len(self.iter_object):
            raise StopIteration

        start_elm = self.iter_object[self.index]
        start_idx = self.index

        for i in range(self.index + 1, len(self.iter_object)):
            val1 = self.key(self.iter_object[i]) if self.key else self.iter_object[i]
            val2 = self.key(start_elm) if self.key else start_elm

            if (self.reverse and val1 > val2) or (not self.reverse and val1 < val2):
                start_elm = self.iter_object[i]
                start_idx = i

        self.iter_object[self.index], self.iter_object[start_idx] = self.iter_object[start_idx], self.iter_object[
            self.index]

        self.index += 1

        return start_elm

    def __iter__(self):
        return self


# lst = 'add', 'fdrfg', '2', 'rr', 'ertewr', '9'
# it = Iterator(lst,lambda x: len(x), True)
# print(lst)
# print(list(it))

# ******************************************************************************************************************

class WordsEager:
    def __init__(self, string: str):
        self.string = string
        self.index = 0

    def __next__(self):
        if self.string == '' and self.string.isspace():
            return print('в строке слов нет')
        lst_is_string = self.string.split()

        while self.index < len(lst_is_string):
            self.index += 1
            return lst_is_string[self.index-1]

        raise StopIteration

    def __iter__(self):
        return self


# it = WordsEager('Реализовать класс WordsEager , принимающий в конструктор строку и выдающий')
# print(list(it))


# ******************************************************************************************************************

class WordsLazy:
    def __init__(self, string: str):
        self.string = string
        self.begin = 0
        self.end = 0

    def __next__(self):
        if not self.string.strip():
            raise StopIteration
        while self.end < len(self.string) and self.string[self.end] ==' ':
            self.end += 1
            self.begin = self.end

        while self.end >= len(self.string):
            raise StopIteration

        while self.end < len(self.string) and self.string[self.end] != ' ':
            self.end += 1

        word = self.string[self.begin : self.end]
        self.begin = self.end

        return word

    def __iter__(self):
        return self

# it = WordsLazy('Реализовать класс WordsEager, принимающий в конструктор строку и выдающий')
# print(list(it))

# ******************************************************************************************************************

class Primes:
    def __init__(self, n=1):
        self.n = self.validate(n)
        self.count = 0

    def validate(self, n):
        if not isinstance(n, int) or n < 1:
            raise TypeError(f'Несоответствие типа данных <class int> или значения n > 1')
        return n

    def __next__(self):
        if self.count < self.n:
            res = rint(2 + self.count, 2 * (self.count + 1))
            self.count += 1
            return res

        raise StopIteration

    def __iter__(self):
        return self

a = Primes()
print(list(a))

