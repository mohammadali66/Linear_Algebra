import numpy as np

# EA = u
E_2_1 = np.matrix([[1,0,0], [-2,1,0], [0,0,1]])
E_3_1 = np.matrix([[1,0,0],[0,1,0],[0,0,1]])
E_3_2 = np.matrix([[1,0,0], [0,1,0], [0,-5,1]])

E = np.matmul(E_3_2,np.matmul(E_3_1, E_2_1))
print('E = E_3_2 * E_3_1 * E_2_1')
print(E)
print('...................................................')

# A = Lu
# L = E_2_1_inv * E_3_1_inv * E_3_2_inv
E_2_1_inv = np.linalg.inv(E_2_1)
E_3_1_inv = np.linalg.inv(E_3_1)
E_3_2_inv = np.linalg.inv(E_3_2)

L = np.matmul(E_2_1_inv, np.matmul(E_3_1_inv, E_3_2_inv))
print(('L = E_2_1_inv * E_3_1_inv * E_3_2_inv'))
print(L)

