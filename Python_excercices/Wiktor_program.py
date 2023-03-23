import random
from random import randint

print('Wiktor dodaje i odejmuje')


class CountWiktor:

    @staticmethod
    def wiktor_random_numbers():
        return [randint(1, 20) for x in range(2)]

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    def adding_subtracting_choice(self):
        choice = random.choice([1, 2])
        if choice == 1:
            return 'Dodawanie'
        return 'Odejmowanie'

    def evaluate_random_numbers(self):
        random_numbers = self.wiktor_random_numbers()
        print(f'Wylosowane liczby to {random_numbers}')
        random_operation = self.adding_subtracting_choice()
        print(f'Wylosowania operacja to {random_operation}')
        if random_operation == 'Dodawanie':
            return f'Wynik dodawania to {self.add(a=random_numbers[0], b=random_numbers[1])}'
        return f'Wynik odejmowania to {self.subtract(a=random_numbers[0], b=random_numbers[1])}'

# clasa = CountWiktor()
# print(clasa.evaluate_random_numbers())


class Tom(CountWiktor):
    def kamil_ma(self):
        CountWiktor().evaluate_random_numbers()

# clasa = Tom()
# print(clasa.evaluate_random_numbers())


class Solution:

    def single_number(self, nums) -> int:
        single = []
        for number in nums:
            if number not in single:
                single.append(number)
            else:
                if number in single:
                    single.remove(number)
        return single[0]

# sol = Solution()
# print(sol.single_number([2,2,1,3,3,4,4]))


list1 = [1,2,4]
list2 = [1,3,4,5,2,6]


class Solution2:
    def merge_and_sort(self, l1=[], l2=[]):
        l1.extend(l2)
        l1.sort()
        return l1

# sol = Solution2()
# mean = sol.merge_and_sort(list1,list2)
# print(mean)


list_compre = [number for number in range(1, 50) if number % 4 == 0]
print(list_compre)
average = round(sum(list_compre) / len(list_compre))
print(f'AV = {average}')

def close_to_average(my_list, my_number):
    # return min(my_list, key=lambda x: abs(x - my_number)) #rozwiazanie z lambda
    z = []
    for x in my_list:
        z.append(abs(x - my_number))
    return my_list[z.index(min(z))]

# return my_list.index(min(z))

print(close_to_average(list_compre, average))


#Write a Python code to reverse a given list.
array = [3, 12, 5, 24, 23, 76, 86, 24, 86, 1, 2]
array2 = ['slo', 'wa', 'cki']

# print(array[])

def revert_list(lst):
    return lst[::-1]

# print(revert_list(array))


#Write a Python program that rotates an array by two positions to the right

def rotate_two_to_right(lst):
    temp = []
    for item in range(2):
        temp.insert(0, lst[-(item+1)])
    temp.extend(lst[2:-2])
    return temp

# print(rotate_two_to_right(array))


#Write a Python program that removes vowels from a string.
stro = 'Java point'
vowelss = ['abc']

def remove_vowels_from_string(string):
    new_word = ''
    vowels = ['a', 'o', 'u', 'i', 'e']
    # splitted = string.strip()
    # breakpoint()
    for letter in string:
        if letter not in vowels:
            new_word += letter
    return new_word

# print(remove_vowels_from_string(stro))


int_to_str = [str(x) for x in array]
int_to_str_2 = list(map(str, array))
print(''.join(int_to_str))
print(int_to_str_2)

# Write program that reverses number
def reverse_number():
    number = 12345
    return int(str(number)[::-1]) -1

# print(reverse_number())

dictt = {x:'el' for x in range(2)}
# print(dictt)

b = array2
b.append('CYC')
# print(array2)





# Question
# a = ['Elo', 'Melo']
# b = a
# print(f'{id(a)} <A, {id(b)} <B ')
# b.append('Mark')
# print(a, b)
# breakpoint()
# print(f'{id(a)} <A, {id(b)} <B ')
# b=['den']
# print(f'{id(a)} <A, {id(b)} <B ')
#
# print(b,a)


# Running Sum
numx = [1,2,3,4]


def sum_num(lst):
    new_lst = []
    for x in range(len(lst)):
        new_lst.append(sum(lst[:x+1]))
    return new_lst


def sum_one_line(lst):
    return [sum(lst[:x+1]) for x in range(len(lst))]

# print(sum_num(numx))

#Extra candies


can = [2,3,5,1,3]
extra = 3


def extra_candies(candies, extra_candie):
    lst =[]
    for candy in candies:
        lst.append(max(candies) <= candy + extra_candie)
    return lst


print(extra_candies(can, extra))


def extra_candies_one_line(candies, extra_candie):
    return [max(candies) <= candy + extra_candie for candy in candies]

# print(extra_candies_one_line(can, extra))


#Shuffle numbers
nume = [2,5,1,3,4,7]
nx = 3

def shufle(nums, n):
    lst = []
    for x in range(len(nums) - n):
        lst += nums[x::n]
    return lst

# print(shufle(nume, nx))
#
# print(len(nume) - nx)

# def duplicats_in_list(lst):
#     return not len(lst) == len((set(lst)))
#
# # print(duplicats_in_list(nume))
#
#
# languages = ['Java', 'Python', 'JavaScript', 'ee', 'rrrr']
# versions = [14, 3, 6, 1, 2, 3]
#
# zyp = zip(languages, versions)
# print(list(zyp))
#
#
# num = [2,2,1,1,1,2,2]
# def majority_number(nums):
#     vc = list(set(nums))
#     majority = 0
#     all_items = 0
#     for item in vc:
#         if nums.count(item) > all_items:
#             all_items = nums.count(item)
#             majority = item
#     return majority
#
# print(majority_number(num))