
"""
Given a list of integers, return the difference between the largest and smallest integers in the list.

Examples
difference([10, 15, 20, 2, 10, 6]) ➞ 18
# 20 - 2 = 18

difference([-3, 4, -9, -1, -2, 15]) ➞ 24
# 15 - (-9) = 24

difference([4, 17, 12, 2, 10, 2]) ➞ 15


"""


def difference(nums):
    mymin = 0
    if nums[0] > 0:
        mymin = nums[0]
    for i in nums:
        if i < mymin:
            mymin = i
           
    mymax = 0
    if nums[0] < 0:
        mymax = nums[0]
    for i in nums:
        if i > mymax:
            mymax = i
    
    return mymax - mymin 