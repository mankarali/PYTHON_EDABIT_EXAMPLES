"""
Censor Words from List
Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.


censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
"""



def censor_string(txt, lst, char):
	X=[]
	Y= txt.split()
	return ' '.join([len(i)*char if i in lst else i for i in Y])