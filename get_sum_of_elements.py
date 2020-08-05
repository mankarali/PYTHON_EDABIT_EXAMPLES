
"""Get the Sum of All List Elements
Create a function that takes a list and returns the sum of all numbers in the list.

get_sum_of_elements([2, 7, 4]) ➞ 13

get_sum_of_elements([45, 3, 0]) ➞ 48

get_sum_of_elements([-2, 84, 23]) ➞ 105

"""


def get_sum_of_elements(lst):
    mysum = 0
    for i in lst:
        mysum = mysum + i
    return mysum
    
get_sum_of_elements([-2, 84, 23])