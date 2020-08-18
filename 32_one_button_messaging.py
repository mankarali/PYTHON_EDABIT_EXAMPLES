"""
One Button Messaging Device
Imagine a messaging device with only one button. For the letter A, you press the button one time, for E, you press it five times, for G, it's pressed seven times, etc, etc.

Write a function that takes a string (the message) and returns the total number of times the button is pressed.

Examples
how_many_times("abde") ➞ 12

how_many_times("azy") ➞ 52

how_many_times("qudusayo") ➞ 123
Notes
Ignore spaces.
"""

def how_many_times(msg):
    
    a = "abcdefghijklmnopqrstuvwxyz"
    
    count = 0
    for i in range(len(a)):
        if a[i] in msg:
            count = count + (i+1)*(msg.count(a[i]))
        
    return count   
        
how_many_times("qudusayo") 