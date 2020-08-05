"""
Xs and Os, Nobody Knows

Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

Return a boolean value (True or False).
The string can contain any character.
When no x and no o are in the string, return True.

xamples
XO("ooxx") ➞ True

XO("xooxx") ➞ False

XO("ooxXm") ➞ True
# Case insensitive.

XO("zpzpzpp") ➞ True
# Returns True if no x and o.

XO("zzoo") ➞ False
"""

def XO(txt):
    x = 0
    o = 0
    
    for i in txt.lower():
        if i == "x":
            x = x + 1
            
        elif i == "o":
            o = o + 1
    if x == o:
        return True
    else :
        return False
    
XO("zpzpzpp") 


