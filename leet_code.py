import collections


# class Solution:
from typing import List


def firstUniqChar( s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    # build hash map : character and how often it appears
    count = collections.Counter(s)
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1

print(firstUniqChar(s='smsietanaaa'))


countries = ['Obszar EuropaObszar Rosja, Kazachstan, MongoliaObszar Azja bez Bliskiego Wschodu, Rosji, Mongolii i KazachstanuObszar Australia i OceaniaObszar Ameryka Północna bez MeksykuObszar Ameryka Środkowa i PołudniowaObszar Afryka PołudniowaObszar Afryka CentralnaObszar Afryka PółnocnaObszar Bliski Wschód']

komputer = {'procesor': 1279, 'karta_g': 2259, 'dysk': 210, 'ram': 250, 'plyta_glowna': 500, 'system': 500, 'obudowa': 350}

print(sum((komputer.values())))
print(komputer.keys())

print(list(komputer.values()))

def isPalindrome( x: int):
    numer_text = str(x)
    revers = ''.join(reversed(numer_text))
    return int(revers) == x


def isPalindrome2(x: int) -> bool:
    return str(x) == str(x)[::-1]
print(isPalindrome(121))


#Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

def romanToInt(s: str):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD",
                                                                                                            "CCCC").replace(
        "CM", "DCCCC")
    for letter in s:
        number += translations[letter]
    return number

print(romanToInt('MCMXCIV'))


strs = ["fieower", "fleow", "fleight", 'flogamina']


def longestCommonPrefix( strs: List[str]) -> str:  # strs = ["flower","flow","flight"]
    short = min(strs, key=len)  # short = "flow"
    for item in strs:  # When item = "flight"
        while len(short) > 0:
            if item.startswith(
                    short):  # during loop 1 condition fails, during loop 2 condition fails, during loop 3 "flight" startswith fl is True
                break
            else:
                short = short[:-1]  # during loop 1 short = flo, during loop 2 short = fl
    return short

#moj rozwiazanie
def longestCommonPrefix(self, strs: List[str]) -> str:
    shortest = str(min(strs, key=len))
    for y in range(len(shortest)):
        for x in strs:
            if x.startswith(shortest):
                continue
            else:
                shortest = shortest[:len(shortest) - 1]
    return shortest

print(longestCommonPrefix(strs))

print(max(komputer.values()))


duplikaty = [5,5,1,1,2,2,3,3,0,0,0,0]

# def removeDuplicates(nums: List[int]) -> int:
#     no_duplicates = []
#     for item in nums:
#         if item in no_duplicates:
#             continue
#         else:
#             no_duplicates.insert(0,item)
#     return no_duplicates

# print(removeDuplicates(nums=duplikaty))

def remove2(nums):
    mlist = list(set(nums))
    # mlist.sort()
    # for i in range(len(mlist)):
    #     nums[i] = mlist[i]
    return len(mlist), mlist

# print(remove2(duplikaty))

# print(list(set(duplikaty)))


slowo = 'aabbccddeeff'
def remove_slowo(slowo):
    slowo1 = ''
    for x in slowo:
        if x in slowo1:
            continue
        else:
            slowo1 += x
    return slowo1


# print(remove_slowo(slowo=slowo))


num_list = [3,2,2,3,1,1,4,4,3]
print(f'TUTAJ INDEX elementu {num_list.index(3)}')
num_list.insert(0,0)
print(num_list)

def removeElement(nums: List[int], val: int):
    while val in nums:
        nums.remove(val)
    return nums

# print(removeElement(nums=num_list, val=3))

nums2 = [1,3,5,6]
nums = [1,3,4,5,6]
target = 7
def searchInsert(nums: List[int], target: int):
    if target in nums:
        return nums.index(target)
    else:
        return [x for x in range(target+1)].index(target)

# print(searchInsert(nums2,target))


def searchInsert2(nums: List[int], target: int):
    if target not in nums:
        nums.append(target)
        nums.sort()
    return nums.index(target)

print(searchInsert2(nums2,target))


s = "   fly me   to   the moon  "
def lengthOfLastWord( s: str):
    lista = s.split(' ')
    re = list(filter(None, lista))
    return len(re[-1])

print(lengthOfLastWord(s=s))


lista_komp = list(komputer.values())
print(lista_komp)
lista_komp.insert(len(lista_komp), '')
print(lista_komp)
print(list(filter(None, lista_komp)))


digits = [2,9,9,9,9]
print(digits[-1])

def plusOne(digits: List[int]):
    if digits[-1] < 9:
        digits[-1] += 1
    else:
        if len(digits) < 1:
            digits[-1] = 0
            digits[-2] += 1
        else:
            breakpoint()
            digits.insert(0,1)
            digits[-1] = 0
    return digits

# def plusOne2(digits):
#     # Adjusting an array of digits into an integer
#     digits_integer = int(''.join(map(str,digits)))
#     digits_integer +=1
#     # Adjusting back an integer into an array of digits after plus 1
#     return [int(x) for x in str(digits_integer)]

# print(plusOne2(digits))

# lista1 = ''.join(map(str, digits))

# print(lista1)

# w = ''.join(lista1)
# print(int(w) )

#
# parzyste = [x for x in range(11) if x % 2 == 0]
# print(parzyste)
#
#
# A = 1,2,3
# a,b,c = A
# import sys
# print(sys.version)

digits = [2,9,9,9,7]

def digits_count(digits):
    x = list(map(str, digits))
    y = int(''.join(x))
    y += 1
    return [int(x) for x in str(y)]

print(f'{digits_count(digits)}  To jest wynik digitcounts')

# def dodaj(number):
#     return number + 1
#
# set_dig= set(digits)
# print(set_dig)
# print(set(map(dodaj, set_dig)))

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(n):
            if n in [1, 2]:
                return n
            return climb(n-1) + climb(n-2)
        return climb(n)

# doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
#
# even_squares = [x**2 for x in range(1, 12) if x % 2 == 0]
#
# cubes_by_four = [x**3 for x in range(1, 11) if (x ** 3) % 4 == 0]


def fibo(n):
    if n in [0, 1]:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(4))


x1 = [fibo(n) for n in range(10)]
# print(x1)
# x2 = list(set(x1))[2:]
# x2.sort()
# print(x2)
# # znajdz srodkową warość
# x3 = round((len(x2) -1) / 2)
# print(x3)
# print(x2[x3])

hashed = 'XLXuX XbXXXiXXe XXXpXXXlX XXaXcXkXi'
unhashed = list(filter(lambda x: x != 'X', hashed))
wx = (''.join(unhashed))

numbers = [x**2 for x in range(10)]
print(numbers)
print(list(filter(lambda x: 9 < x < 50, numbers)))

print(wx.replace(' ', '--'))

#Write a Python code to reverse a given list.