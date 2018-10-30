# inverses for sequence matrices
# Gouss Jordan (solve 2 equations at once)

import numpy as np

A = np.matrix([[1,3], [2,6]])
I = np.identity(2)

# concatenate A & I
AI = np.concatenate((A,I), axis=1)
print('AI:')
print(AI)
print('......................')

E_2_1 = np.matrix([[1,0], [-2,1]])
A_changed = np.matmul(E_2_1, A)
I_changed = np.matmul(E_2_1, I)
AI_changed = np.concatenate((A_changed, I_changed), axis=1)
print('AI level1:')
print((AI_changed))
print('......................')

E_1_2 = np.matrix([[1,-3], [0,1]])
A_changed = np.matmul(E_1_2, A_changed)
I_changed = np.matmul(E_1_2, I_changed)
AI_changed = np.concatenate((A_changed, I_changed), axis=1)
print('AI level2:')
print((AI_changed))

print('......................')
print('A inverse is:')
print(I_changed)
