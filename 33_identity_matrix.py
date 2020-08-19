"""
Identity Matrix
An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.

Examples
id_mtrx(2) ➞ [
  [1, 0],
  [0, 1]
]

id_mtrx(-2) ➞ [
  [0, 1],
  [1, 0]
]

id_mtrx(0) ➞ []
Notes
Incompatible types passed as n should return the string "Error".


Test.assert_equals(id_mtrx(1), [[1]])
Test.assert_equals(id_mtrx(2), [[1, 0], [0, 1]])
Test.assert_equals(id_mtrx(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
Test.assert_equals(id_mtrx(4), [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
Test.assert_equals(id_mtrx(-6), [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]])
Test.assert_equals(id_mtrx("edabit"), "Error", 'Incompatible types passed as n should return the string "Error".')

"""
def id_mtrx(n):
    if not isinstance(n,int):
        return "Error"
    
    a = []
    b = []
    if n > 0:
        for i in range(n):
            for j in range(n):
                if i == j:
                    a.append(1)
                else:
                    a.append((0))

        for i in range(n):
            b.append(a[n*i:n*i+n])
        return (b)

    elif n < 0:
        for i in range(abs(n)):
            for j in range(abs(n)):
                if i == abs(n)-j-1:
                    a.append(1)
                else:
                    a.append((0))
         
        for i in range(abs(n)):
            b.append(a[abs(n)*i:abs(n)*i+abs(n)])
        return (b)
        
    else:
        return []
        
id_mtrx(-6)