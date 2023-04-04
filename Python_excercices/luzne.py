import json
from typing import Optional


def open_json_data():
    with open('../test_forex/data/data.json') as file:
        return json.load(file)
pd = open_json_data()
# w = {'AED': 'United Arab Emirates Dirham'}

l1 = [2, 4, 3]
l2 = [5, 6, 4]
l3 = [9,9,9,9,9,9,9]
l4 = [9,9,9,9]


# Odwrocic int w listach i dodac do siebie, zwrocic liste z podzielonym intem od tylu
class Solution:

    def addTwoNumbers(self, l1: list, l2: list) -> list:
        # number1 = list(map(str, l1))[::-1]
        number1 = [str(x) for x in l1][::-1]
        number2 = [str(x) for x in l2][::-1]
        n1_conv = int(''.join(number1))
        n2_conv = int(''.join(number2))
        result = n1_conv + n2_conv
        result_string = list(str(result)[::-1])
        result_int = [int(x) for x in result_string]
        return result_int


print(Solution().addTwoNumbers(l1=l3, l2=l4))


# najczesciej wystepujaca liczba na liscie
import statistics
ls1 = [21,13,19,3,11,5,18]
mode = statistics.mode(ls1)
print(f'Najczesciej wystepujaca liczba na liscie to {mode}')

# sredia z listy
srednia = statistics.mean(ls1)
print(srednia)

# mediana listy
median = statistics.median(ls1)
print(median)


#Jaka bedzie dlugość po splicie 2 czy 3 ?
slowo = 'abc%def%'
slowo2 = len(slowo.split('%'))
print(f'Dlugosc listy po podziale {slowo2}')



# FIFO in python queue
# Initializing a queue
def fifo():
    queue = []

    # Adding elements to the queue
    queue.append('a')
    queue.append('b')
    queue.append('c')

    print("Initial queue")
    print(queue)

    # Removing elements from the queue
    print("\nElements dequeued from queue")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    print("\nQueue after removing elements")
    print(queue)

list_back = list(reversed(range(1,11)))
print(f'Lista od 1 do 10 od tylu \n{list_back}')

list_back.pop(0)

print(list_back)
list_back.remove(3)
print(list_back)

