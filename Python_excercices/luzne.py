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

# num1 = 5
# num2 = 2
# if num2 < num1:
#     raise ValueError('ELo')
# else:
#     raise Exception('To jest blad')


# for x in range(5):
#     try:
#         assert 1 == 2
#     except AssertionError:
#         raise Exception('Error')

