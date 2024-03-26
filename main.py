""" CyclicIterator"""


class CyclicIterator:
    """CyclicIterator"""
    def __init__(self, obj):
        self.object = obj
        self.obj = iter(obj)
        self.el = next(self.obj)

    def __iter__(self):
        return self

    def peak(self):
        """next value"""
        return self.el

    def __next__(self):
        result = self.el
        try:
            self.el = next(self.obj)
        except StopIteration:
            self.obj = iter(self.object)
            self.el = next(self.obj)
        return result


cycle_iter = CyclicIterator([1, 2, 3])
print(next(cycle_iter))
print(cycle_iter.peak())
print(next(cycle_iter))
# print(cycle_iter.peak())
print(next(cycle_iter))
# print(next(cycle_iter))
print(cycle_iter.peak())
# print(cycle_iter.peak())
print(next(cycle_iter))
# print(cycle_iter.peak())
