l1 = [str(x) for x in range(1, 10) if x % 2 != 0]
l2 = [str(x) for x in range(1, 20) if x % 2 == 0]
l_zip = list(zip(l1, l2))


for big, bigger in zip(l1, l2):
    print(f'First {big}, second {bigger}')


l3 = [1,2,3]
print(id(l3))

l4 = l3[:]

print(id(l4))