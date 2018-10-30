# matrices multiplication have 4 ways :
import numpy as np

A = np.matrix([[1,2,3], [2,3,4]])
B = np.matrix([[8,7,4,3], [2,1,2,3], [1,1,0,2]])

# C = A.B
# A.shape is a tuple for size of matrix ----> (row, column)

# 1st method :
# C(1,2) :
C_1_2 = 0
for i in range(A.shape[1]):
    C_1_2 += A[1,i] * B[i,2]

print('first method:')
print('C[1,2]: ', C_1_2)
print('......................................')

# 4th methond :
# C = A.B is sum of (columns of A) * (rows of B)
A = np.matrix([[2,7], [3,8], [4,9]])
B = np.matrix([[1,6], [0,0]])

C = np.matmul(A[:,0], B[0,:]) + np.matmul(A[:,1], B[1,:])
print('forth method:')
print('C = A.B: ')
print(C)
