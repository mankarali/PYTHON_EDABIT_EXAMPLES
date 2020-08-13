"""
Check for Anagrams
Create a function that takes two strings and returns either True or False depending on whether they're anagrams or not.

Examples
is_anagram("cristian", "Cristina") ➞ True

is_anagram("Dave Barry", "Ray Adverb") ➞ True

is_anagram("Nope", "Note") ➞ False
Notes
Should be case insensitive.
The two given strings can be of different lengths.
"""

def is_anagram(s1, s2):
    a = sorted(list(s1.lower()))
    b = sorted(list(s2.lower()))

    
    if a == b:
        return True
    else:
        return False
    
is_anagram("Dave Barry", "Ray Adverb")    