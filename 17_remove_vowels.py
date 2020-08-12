"""
Remove Every Vowel from a String
Create a function that takes a string and returns a new string with all vowels removed.

Examples
remove_vowels("I have never seen a thin person drinking Diet Coke.")
➞ " hv nvr sn  thn prsn drnkng Dt Ck."

remove_vowels("We're gonna build a wall!")
➞ "W'r gnn bld  wll!"

remove_vowels("Happy Thanksgiving to all--even the haters and losers!")
➞ "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"
Notes
"y" is not considered a vowel.
Expect a valid string for all test cases.
"""
def remove_vowels(txt):
    
    a = list(txt)
    b = "aeuioAEUIO"
    
    for i in txt:
        if i in b:
            a.remove(i)

    return ("".join(a))


remove_vowels("We're gonna build a wall!")