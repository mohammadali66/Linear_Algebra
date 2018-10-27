import numpy as np

'''
    x   + 2*y + z = 2
    3*x + 8y  + z = 12
          4*y + z = 2
'''

A = np.matrix([[1,2,1], [3,8,1], [0,4,1]])
b = np.array([2,12,2])

E_2_1 = np.matrix([[1,0,0], [-3,1,0], [0,0,1]])

print('A * E_1_1:')
u_2_1 = np.matmul(E_2_1, A)
print(u_2_1)
