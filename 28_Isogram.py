"""
Is the Word an Isogram?
An isogram is a word that has no repeating letters, consecutive or nonconsecutive. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

Examples
is_isogram("Algorism") ➞ True

is_isogram("PasSword") ➞ False
# Not case sensitive.

is_isogram("Consecutive") ➞ False
Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings.
"""
def is_isogram(txt):
    a = txt.lower()
    b = []
    b.append(a[0])
    for i in range(1, len(a)):
        if a[i] in b:
            return False
            break
        b.append(a[i])    
    return True

is_isogram("Algorism")