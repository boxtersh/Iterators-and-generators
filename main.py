from typing import Callable, Any, Union
from random import randint as rint


# ******************************************************************************************************************
# 1. Iterator Sorted
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
