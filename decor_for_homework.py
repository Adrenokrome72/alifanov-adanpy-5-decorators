from datetime import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'Время вызова функции: {datetime.now().strftime("%d-%m-%Y, %H:%M:%S")},'
                        f'название функции: {old_function.__name__}, аргументы: {args} {kwargs},'
                        f'результат: {result}\n')
            return result
        return new_function
    return __logger

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cursor = 0
        self.subcursor = 0

    def __iter__(self):
        return self

    @logger('main.log')
    def __next__(self):
        if self.cursor == len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.cursor][self.subcursor]
        if self.subcursor == len(self.list_of_list[self.cursor]) - 1:
            self.cursor += 1
            self.subcursor = 0
        else:
            self.subcursor += 1
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()