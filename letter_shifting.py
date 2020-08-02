
"""
Letter Shifting

Create a function that takes a string and shifts the letters to the right by an amount n but not the whitespace.

Examples
shift_letters("Boom", 2) ➞ "omBo"

shift_letters("This is a test",  4) ➞ "test Th i sisa"

shift_letters("A B C D E F G H", 5) ➞  "D E F G H A B C"
Notes
Keep the case as it is.
n can be larger than the total number of letters.

"""





def shift_letters(txt, n):
    a = "".join(txt.split())
    a = list(a[-n%len(a):] + a[:-n%len(a)])
    return ''.join(a.pop(0) if i != ' ' else i for i in txt)