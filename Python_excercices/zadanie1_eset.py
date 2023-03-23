import timeit

# The order of chars is important.
input_str = 'bbbadcaba'
# Expected result:
# output = 'badc'
# 'cabd' - wrong output


def unique(input_s):
    str = ''
    for x in input_s:
        if x not in str:
            str += x
    return str


print(unique(input_str))

#czy mozna to inaczej zaprojektowac, wartosc obliczeniowa

rep1 = input_str.replace('bbb', 'b').replace('aba', '')
rep2 = input_str[2:-3]

print(rep2)


# print(timeit.timeit(unique('s'), number=100))




