"""
The Perrin Sequence

Each number in the Perrin sequence is created by summing the numbers two positions and three positions before it. The first three numbers are (3, 0, 2), and the sequence is extended as follows:

P(0) P(1) P(2) P(3) P(4) P(5) P(6) P(7) ... P(n)
3, 0, 2, 3, 2, 5, 5, 7, ...
Given a value for n, return the Perrin number P(n).


Examples
perrin(1) ➞ 0

perrin(8) ➞ 10

perrin(26) ➞ 1497

"""



def censor_string(txt, lst, char):
	X=[]
	Y= txt.split()
	return ' '.join([len(i)*char if i in lst else i for i in Y])