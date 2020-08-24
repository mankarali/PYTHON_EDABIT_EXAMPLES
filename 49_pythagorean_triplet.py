"""
Pythagorean Triplet
Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

Examples
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25

is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169

is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9
Notes
Numbers may not be given in a sorted order.
"""
def is_triplet(n1, n2, n3):
    
    a = [n1, n2, n3]
    b = sorted(a)

    if b[0]**2 + b[1]**2 == b[2]**2:
        return True
    return False
    
    
    
is_triplet(13, 5, 12)    