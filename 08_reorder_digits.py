"""Reorder Digits
Create a function that reorders the digits of each numerical element in a list based on ascending (asc) or descending (desc) order.

Examples
reorder_digits([515, 341, 98, 44, 211], "asc") ➞ [155, 134, 89, 44, 112]

reorder_digits([515, 341, 98, 44, 211], "desc") ➞ [551, 431, 98, 44, 211]

reorder_digits([63251, 78221], "asc") ➞ [12356, 12278]

reorder_digits([63251, 78221], "desc") ➞ [65321, 87221]

reorder_digits([1, 2, 3, 4], "asc")  ➞ [1, 2, 3, 4]

reorder_digits([1, 2, 3, 4], "desc") ➞ [1, 2, 3, 4]
"""


def reorder_digits(lst, direction): 
    return [int(''.join(sorted(str(i),reverse=direction=="desc"))) for i in lst]