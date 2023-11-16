# Task1

def with_index(iterable, start=0):
    index = start
    for element in iterable:
        yield index, element
        index += 1


# Task2

def my_range(*args):
    start, stop, step = 0, None, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
        if step < 0:
            start, stop = stop, start
    else:
        raise TypeError(f'my_range expected at most 3 arguments, got {len(args)}')

    current = start
    while (stop is None) or (current < stop if step > 0 else current > stop):
        yield current
    current += step


# Task 3

class MyIter:
    def __init__(self, obj):
        self.obj = list(obj)
        self.max_value = len(obj)
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.max_value:
            obj = self.obj[self.current_value]
            self.current_value += 1
            return obj
        else:
            raise StopIteration
