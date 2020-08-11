"""
Vowel Replacer
Create a function that replaces all the vowels in a string with a specified character.

Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
"""

def replace_vowels(txt, ch):
    
    v = "aeiou"
    
    a=[]
    for i in txt:
        if not i in list(v):
            a.append(i)
        else:
            a.append(ch)
    return "".join(a)

replace_vowels("minnie mouse", "?")