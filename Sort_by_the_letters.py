"""
Write a function that sort each string in a list by the letter in alphabetic ascending order (a-z).
Examples
sort_by_letter(["932c", "832u32", "2344b"])
➞ ["2344b", "932c", "832u32"]

sort_by_letter(["99a", "78b", "c2345", "11d"])
➞ ["99a", "78b", "c2345", "11d"]

sort_by_letter(["572z", "5y5", "304q2"])
➞ ["304q2", "5y5", "572z"]

sort_by_letter([])
➞ []
Notes
Each string will only have one (lowercase) letter.
If given an empty list, return an empty list.

"""



def sort_by_letter(lst):
    return sorted(lst, key = lambda a: "".join([k for k in a if k.isalpha()]))