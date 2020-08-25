"""
Regex Series: String Contains at Least One Digit
Write a regular expression that matches a string if it contains at least one digit.

Examples
has_digit("c8") ➞ True

has_digit("23cc4") ➞ True

has_digit("abwekz") ➞ False

has_digit("sdfkxi") ➞ False
Notes
This challenge is designed to use RegEx only.
"""
import re

def has_digit(txt):
    
    x = re.findall("[0-9]", txt)
    if x:
        return (True)
    else:
        return (False)
   
    
has_digit("23cc4")    
    