"""
Most Left Digit
Write a function that takes a string as an argument and returns the left most integer in the string.

Examples
left_digit("TrAdE2W1n95!") ➞ 2

left_digit("V3r1ta$") ➞ 3

left_digit("U//DertHe1nflu3nC3") ➞ 1

left_digit("J@v@5cR1PT") ➞ 5
Notes
Each string will have at least two numbers.
"""

def left_digit(num):
    a = []
    digit = "0123456789"
    for i in num:
        if i in digit:
            a.append(i)
    return int(a[0])


left_digit("U//DertHe1nflu3nC3") 