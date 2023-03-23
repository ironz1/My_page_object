
def more_than_5(x):
    if x > 5:
        print('Its more than Five')
    else:
        raise Exception('Its less than 5')


lista = [x for x in range(1, 10) if x % 2 == 1]
print(lista)


def odds_to_power(x):
    return x ** 2

lista2 = list(map(odds_to_power,lista))

print(lista2)


def filtr_5_to_15(item):
    if 30 > item > 5:
        return item

print(list(filter(filtr_5_to_15,lista2)))


def fibo(x):
    if x < 2:
        return x
    return fibo(x-1) + fibo(x-2)


lista_f = [x for x in range(1, 10)]
fibo_list = list(map(fibo, lista_f))
print(f'Lista fibo {fibo_list}')
average = round(sum(fibo_list) / len(fibo_list))
print(f'Srednia {average}')


def close_to_average():
    empty = []
    for x in fibo_list:
        empty.append(abs(x - average))
    return fibo_list[empty.index(min(empty))]

# print(close_to_average())


def context_write_outcome():
    with open('../fibo.txt', 'w+') as file1:
        file1.write(f'This is average of list {average}\n')
        file1.write(f'Score closest to the average {str(close_to_average())}')

# context_write_outcome()

lista3 = lista


list4 = (list(map(lambda x: x + 1 , lista3)))

listr_str = ['a', 'b', 'c']

# print(lista2)

import time

def dekor(funkcja):
    def wew(*args, **kwargs):
        start = time.time()
        x = funkcja(*args, **kwargs)
        koniec = time.time()
        print(funkcja.__name__, "wykonywała się", koniec - start, "sekund.")
        return x
    return wew


@dekor
def change_to_fizz(lis):
    for i,item in enumerate(lis):
        if item % 5 == 0:
            lis[i] = 'buzz'
        elif item % 3 == 0:
            lis[i] = 'fiz'
        elif item % 7 == 0:
            lis[i] = 'fizbuzz'
    return lis


print(change_to_fizz(lista2))

print(list(filter(lambda x: x % 2 == 0, list4)))


test_str = "GeeksForGeeks"


@dekor
def remove_letter(str, index):
    new = ''
    for number in range(len(str)):
        if number != index:
            new += str[number]
    return new


print(remove_letter(test_str, 4))


# Yeld
# def liczby():
#     for i in range(11):
#         yield i * 2
#
#
# for parzysta in liczby():
#     print(parzysta)


xo = '5.000'
x_flo = float(xo)
print(x_flo)


print(list(map(float, ['1', '2', '3'])))

x = ['111','ff']

short = min(x, key=len)
long = max(x, key=len)
print(short, long)