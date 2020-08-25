"""
Count and Identify Data Types
Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.

List order is:

[int, str, bool, list, tuple, dictionary]
Examples
count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]

count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]

count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]

count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]
Notes
If no arguments are given, return [0, 0, 0, 0, 0, 0]
"""

def count_datatypes(*args):
    a=list(args)
    
    if a == []:
        return [0, 0, 0, 0, 0, 0]
   
    k1=0
    k2=0
    k3=0
    k4=0
    k5=0
    k6=0
    
    b=[]
    
    for i in a:
        
        if type(i) is int:
            k1 += 1            
        if type(i) is str:
            k2 += 1           
        if type(i) is bool:
            k3 += 1            
        if type(i) is list:
            k4 += 1
        if type(i) is tuple:
            k5 += 1            
        if type(i) is dict:
            k6 += 1            

    b.append(k1)         
    b.append(k2)
    b.append(k3)    
    b.append(k4)
    b.append(k5)    
    b.append(k6)
    
    return (b)
    
count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6])