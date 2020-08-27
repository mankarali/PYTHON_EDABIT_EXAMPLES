"""
Perimeters With a Catch
Write a function that takes a number and returns the perimeter of either a circle or a square. 
The input will be in the form (letter, number) where the letter will be either s for square, or c for circle, and the number will be the side of the square, or the radius of the circle. Use the following formulas:

Perimeter of a square: 4 * side.
Perimeter of a circle: 6.28 * radius.
The catch is: you can only use arithmetic or comparison operators. That means:

No if... else statements.
No dictionaries.
No lambdas.
No formatting methods, etc.
The goal is to write a short, branch-free piece of code.

Examples
perimeter('s', 7) ➞ 28

perimeter('c', 4) ➞ 25.12
Notes
No rounding needed.
Hint: A False Boolean, used with artihmetic operators, counts as 1, while a False Boolean counts as 0. 
That means (a>b)+1 will return 1 or 2, depending on the values of a and b.
"""
def perimeter(l, num):
       
    return ((l=="s")*4*num) + (l=="c")*6.28*num
    

perimeter('c', 30)
