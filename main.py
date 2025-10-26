from typing import Callable, Any, Union


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



