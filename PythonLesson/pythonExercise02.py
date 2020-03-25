import itertools
from array import array
from functools import reduce
import functools
import math


# 鸭子类型
class Vector(object):
    typecode = 'd'

    def __init__(self, components):
        self._components = array(typecode, components)

    def __hash__(self):
        hash_list = map(lambda x: hash(x), self._components)
        return reduce(lambda a,b: a^b, hash_list, 0)

    def __eq__(self, v):
        return tuple(self) == tuple(self) and all(a == b for a, b in zip(self, v))  # 由于all函数的原因，性能较差

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self._components))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, int):
            return self._components[index]
        else:
            raise TypeError(f"{cls, __name__}")


class CalculabilityMixin:
    def plus(self, v):
        cls = type(self)
        return cls([x + y for x, y in itertools.zip_longest(self, v, fillvalue=0)])




