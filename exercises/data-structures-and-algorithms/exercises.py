# 1. Make a list of the largest or smallest N items from another list

# Input:
# N = 3
numbers = [34, 24, 2, 56, 7, 10, -1, -34, 8, 17]

# Output:
# [56, 34, 24] and [-34, -1, 2]


# 2. Make a list of the largest or smallest N items from another list based on a specific key.

# Input:
# N = 2, key = 'price'
companies = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YAHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# Output:
# [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}]


# 3. Implement a Priority Queues using two OOP classses.
class PriorityQueue:
    # TODO
    pass


class Item:
    # TODO
    pass


# 4. Find the minimum and maximum value from the dictionary below and then sort them ascending and
# descending.
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


# 5. Find out:
# - the common keys from the dictionaries below
# - the common values from the dictionaries below
# - the keys that are in the first dictionary and are missing in the second
#
# Use one-liners !

first = {
    "a": 10,
    "b": 21,
    "c": 8,
}

second = {
    "b": 42,
    "d": 10,
    "a": 5,
}


# 6. Create a function that generates a new dictionary from another dictionary without
# certain keys.
# Example:

initial_dict = {
    "apple": 10,
    "microsoft": 23,
    "google": 98,
    "amazon": 46,
    "dell": 41,
}

# I want to remove "apple" and "microsoft" =>
final_dict = {
    "google": 98,
    "amazon": 46,
    "dell": 41,
}


# 7. Having the below text, create two named slices that extract the two relevant phrases:
# Do you know why are named slices useful ?
wierd_text = "jifrheughreidyrthisisarainydaygtjighiejdenotgreatnotterrible"


# 8. Determine the most frequently occuring items in the next sequence:
# Hint: use collections library.
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

# Using the solution above, find out the number of occurrences for word "eyes".


# 9. Generate a new dictionary (as a subset of another dictionary) taking into consideration
# only values greater than 100. Solve this exercise using an one-liner.
initial_dictionary = {
    "cisco": 200,
    "juniper": 94,
    "checkpoint": 78,
    "paloalto": 86,
    "fortinet": 145,
}


# 10. Group these entries by the date aand print the output in a nice way :).
# Hint: read about itertools library
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
