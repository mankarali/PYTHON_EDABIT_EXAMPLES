"""
String to Dictionary
Create a function that takes a list of strings and returns a dictionary.

Examples
str_to_dict(["1=one", "2=two", "3=three", "4=four"]) ➞ {"1": "one", "2": "two", "3": "three", "4": "four"}

str_to_dict(["dog=bark", "cat=meow", "cow=moo"]) ➞ {"dog": "bark", "cat": "meow", "cow": "moo"}

str_to_dict(["bob=human", "lola=dog", "mittens=cat", "todd=frog"]) ➞ {"bob": "human", "lola": "dog", "mittens": "cat", "todd": "frog"}
Notes
Key and value with be separated with =.
Input list will be of various lengths.
The key will be the first element in the string and the value with be the second
"""
def str_to_dict(lst):
        
    a=[]
    b=[]
    for i in lst:
        a.append(i.split("=")[0])
        b.append(i.split("=")[1])
    
    dct = {}
    
    for i in range(len(lst)):
        dct[a[i]] = b[i]
        
    return (dct)
    
    
str_to_dict(["1=one", "2=two", "3=three", "4=four"])