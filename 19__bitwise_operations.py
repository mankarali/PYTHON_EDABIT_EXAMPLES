"""
Bitwise Operations
A decimal number can be represented as a sequence of bits. To illustrate:

6 = 00000110
23 = 00010111
From the bitwise representation of numbers, we can calculate the bitwise AND, bitwise OR and bitwise XOR. Using the example above:

bitwise_and(6, 23) ➞ 00000110

bitwise_or(6, 23) ➞ 00010111

bitwise_xor(6, 23) ➞ 00010001
Write three functions to calculate the bitwise AND, bitwise OR and bitwise XOR of two numbers.

Examples
bitwise_and(7, 12) ➞ 4

bitwise_or(7, 12) ➞ 15

bitwise_xor(7, 12) ➞ 11



Test.assert_equals(bitwise_and(32, 17), 0)
Test.assert_equals(bitwise_or(32, 17), 49)
Test.assert_equals(bitwise_xor(32, 17), 49)

Test.assert_equals(bitwise_and(13, 19), 1)
Test.assert_equals(bitwise_or(13, 19), 31)
Test.assert_equals(bitwise_xor(13, 19), 30)
"""



def bitwise_and(n1, n2):
    m = "%08d" % int(bin(n1)[2:])
    n = "%08d" % int(bin(n2)[2:])
    
    p = []
    for i in range(8):
        if m[i] == n[i]:
            p.append(int(m[i]))
        else:
            p.append(0)
    p10 = p[0]*128 + p[1]*64 + p[2]*32 + p[3]*16 + p[4]*8 + p[5]*4 + p[6]*2 + p[7]*1
    return p10


def bitwise_or(n1, n2):
    m = "%08d" % int(bin(n1)[2:])
    n = "%08d" % int(bin(n2)[2:])
    r = []
    for i in range(8):
        if int(m[i])==1 or int(n[i])==1:
            r.append(1)
        else:
            r.append(0)
    r10 = r[0]*128 + r[1]*64 + r[2]*32 + r[3]*16 + r[4]*8 + r[5]*4 + r[6]*2 + r[7]*1
    return r10
    

def bitwise_xor(n1, n2):
    m = "%08d" % int(bin(n1)[2:])
    n = "%08d" % int(bin(n2)[2:])
    
    p = []
    for i in range(8):
        if m[i] == n[i]:
            p.append(int(m[i]))
        else:
            p.append(0)
    p10 = p[0]*128 + p[1]*64 + p[2]*32 + p[3]*16 + p[4]*8 + p[5]*4 + p[6]*2 + p[7]*1    
    
    r = []
    for i in range(8):
        if int(m[i])==1 or int(n[i])==1:
            r.append(1)
        else:
            r.append(0)
    r10 = r[0]*128 + r[1]*64 + r[2]*32 + r[3]*16 + r[4]*8 + r[5]*4 + r[6]*2 + r[7]*1
    return (r10-p10)

    
bitwise_and(7, 12)

bitwise_or(7, 12)

bitwise_xor(7, 12)    

