from typing import Callable, Any, Union
from random import randint as rint


# ******************************************************************************************************************
# 1. Iterator Sorted
from typing import Union, Callable, Any

class Sorted:
    def __init__(self,
                 iter_object,
                 key = lambda x: x,
                 reverse = False):
        self.data = list(iter_object)
        self.key = key
        self.reverse = reverse
        self.ind = 0
        self.sorted_data = self._bubble_sort(self.data, self.key, self.reverse)

    def _bubble_sort(self, lst, key, reverse) -> list:
        n = len(lst)
        for i in range(n):
            for j in range(0, n-i-1):
                if (key(lst[j]) > key(lst[j+1])) and not reverse or \
                    (key(lst[j]) < key(lst[j+1])) and reverse:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    def __next__(self):
        if self.ind >= len(self.sorted_data):
            raise StopIteration
        result = self.sorted_data[self.ind]
        self.ind += 1
        return result

    def __iter__(self):
        return self



# lst = 'add', 'fdrfg', '2', 'rr', 'ertewr', '9'
# it = Iterator(lst,lambda x: len(x), True)
# print(lst)
# print(list(it))

# ******************************************************************************************************************
# 2. Iterator Words (версия A — жадная)
class WordsEager:
    def __init__(self, string: str):
        self.string = string
        self.index = 0

    def __next__(self):
        if self.string == '' and self.string.isspace():
            return
        lst_is_string = self.string.split()

        while self.index < len(lst_is_string):
            self.index += 1
            return lst_is_string[self.index - 1]

        raise StopIteration

    def __iter__(self):
        return self


# it = WordsEager('Реализовать класс WordsEager , принимающий в конструктор строку и выдающий')
# print(list(it))


# ******************************************************************************************************************
# 3. Iterator Words (версия B — ленивый)

class WordsLazy:
    def __init__(self, string: str):
        self.string = string
        self.begin = 0
        self.end = 0

    def __next__(self):
        if not self.string.strip():
            raise StopIteration
        while self.end < len(self.string) and self.string[self.end] == ' ':
            self.end += 1
            self.begin = self.end

        while self.end >= len(self.string):
            raise StopIteration

        while self.end < len(self.string) and self.string[self.end] != ' ':
            self.end += 1

        word = self.string[self.begin: self.end]
        self.begin = self.end

        return word

    def __iter__(self):
        return self


# it = WordsLazy('Реализовать класс WordsEager, принимающий в конструктор строку и выдающий')
# print(list(it))

# ******************************************************************************************************************
# 4. Iterator Primes

class Primes:
    def __init__(self, n=1):
        self.n = self.validate(n)
        self.count = 0
        self.prime = 1
        self.flag = False

    def validate(self, n):
        if not isinstance(n, int) or n < 1:
            raise StopIteration
        return n

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        if self.n != 1:
            if self.flag:
                while True:
                    self.prime += 2
                    for dev in range(3, int(self.prime ** 0.5) + 1, 2):
                        if self.prime % dev == 0:
                            break
                    else:
                        self.count += 1
                        return self.prime

            self.flag = True
            self.count += 1
            return 2

        self.count += 1
        return 2

    def __iter__(self):
        return self


# a = Primes(3)
# print(set(a))
# ******************************************************************************************************************
# 5. Generator chunked

def chunked(iterable, size):
    for i in range(0, len(iterable), size):
        if i > len(iterable) - 1:
            return
        yield tuple(iterable[i:i + size])


# ch = chunked('jhvvlulkibghigiyfygvvuvyuyuly', 4)
# print(list(ch))

# ******************************************************************************************************************
# 6. Generator words_generator
def words_generator(text):
    text = text.strip()
    ind_start, ind_end = 0, 0
    if not text:
        return
    while ind_end < len(text):
        if text[ind_end] == ' ':
            yield text[ind_start:ind_end]
            text = text[ind_end:].strip()
            ind_end = 0

        ind_end += 1

    yield text[ind_start:]


# text = '        513     8           13             913 '
# print(tuple(words_generator(text)))

# ******************************************************************************************************************
# 7. Generator primes_in_range

def primes_in_range(start, stop):
    if start >= stop or start <= 1:
        return

    if start == 2:
        yield start

    start = start + 1 if start % 2 == 0 else start

    for prime in range(start, stop + 1, 2):
        for dev in range(3, int(prime ** 0.5), 2):
            if prime % dev == 0:
                break
        else:
            yield prime

# generator = primes_in_range(2, 30)
# print(*list(generator), sep='\n')
