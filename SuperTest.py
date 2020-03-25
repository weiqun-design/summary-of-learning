

class Base:
    def __init__(self):
        print("init Base")


class A(Base):
    def __init__(self):
        super().__init__()
        print("init A")


class B(Base):
    def __init__(self):
        super().__init__()
        print("init B")


class C(A,B):
    def __init__(self):
        super(B,self).__init__()
        print("init C")


c = C()
print(C.mro())