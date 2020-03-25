import math

"""
    单下划线开头 _x 
    双下划线开头 __x
    单下划线结尾
    
    鸭子类型，只要方法实现即可认为真实可用
"""

class Vector:
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return str(tuple(self))

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        """
        对应repr函数的返回值
        :return: Vector(x,y)
        """
        return f"{0}(({1}),({2}))".format(type(self).__name__, self.x, self.y)

    def __hash__(self):
        """
        对应hash函数
        :return:
        """
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        """对应abs函数"""
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


if __name__ == '__main__':
    v1 = Vector(1, 2)
    print(repr(v1))
    print(hash(v1))
    print(abs(v1))
    if v1:
        print(True)
