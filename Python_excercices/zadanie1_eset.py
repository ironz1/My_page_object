
# The order of chars is important.

input_str = 'bbbadcaba'

# Expected result:
# output = 'badc'
# 'cabd' - wrong output


def unique(input_str):
    str = ''
    for x in input_str:
        if x not in str:
            str += x
    return str


print(unique(input_str))

#czy mozna to inaczej zaprojektowac, wartosc obliczeniowa

repla = input_str.replace('bbb', 'b').replace('aba', '')

print(repla)


new_list = list(input_str)
print(new_list)
print(''.join(list(set(new_list))))




