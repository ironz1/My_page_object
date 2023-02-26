class A:
    def print_x(self):
        print('x: A')


class B(A):
    def print_x(self):
        print('x: B')

class C(A):
    def print_x(self):
        print(('x: C'))

class D(B, C):
    pass

d = D()
print(d.print_x())