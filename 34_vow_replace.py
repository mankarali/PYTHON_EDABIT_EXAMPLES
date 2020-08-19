"""
Apples and Bananas
Write a function, that replaces all vowels in a string with a specified vowel.

Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"

vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"

vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
Notes
All words will be lowercase. Y is not considered a vowel.
"""


def vow_replace(word, vowel):
    v = "aeuio"
    a = []
    
    for i in word.lower():
        if i in v:
            a.append(vowel)
        else:
            a.append(i)
    
    return ("".join(a))


    
    
vow_replace("apples and bananas", "u")