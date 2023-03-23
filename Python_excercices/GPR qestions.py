class A:
    def print_x(self):
        print('x: A')


class B(A):
    def print_x(self):
        print('x: B')

class C(A):
    def print_x(self):
        print(('x: C'))

class D(C, A):
    pass

d = D()
print(d.print_x())

######################

class C:

    dangerous = 2

c1 = C()
c2 = C()

c1.dangerous = 5

print(c1.dangerous, c2.dangerous)

del c1.dangerous

print(c1.dangerous)
C.dangerous = 5
print(c2.dangerous)


######

names = ['Yang', 'Forest', 'steve', 'jack']
name_num = {id: name for id, name in enumerate(names) if name[0].isupper()}
print(name_num)
