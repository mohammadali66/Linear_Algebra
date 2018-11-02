import numpy as np

A = np.matrix([[2,1], [8,7]])

E_2_1 = np.matrix([[1,0], [-4,1]])

u = np.matmul(E_2_1, A)
print('E_2_1 * A = u')
print(u)
print('....................................')

#........................................................................
# L = inverse of E_2_1
L = np.linalg.inv(E_2_1)

# A = L * u
A2 = np.matmul(L, u)
print('A = L * u')
print(A2)
print('....................................')

#........................................................................
# A = L * D * u
D = np.matrix([[2,0], [0,3]])
u2 = np.matrix([[1,0.5], [0,1]])
A3 = np.matmul(np.matmul(L,D), u2)
print('A = L * D * u')
print(A3)
