import numpy as np

# exchange rows 1 and 2:
A = np.matrix([[1,2], [3,4]])
per1 = np.matrix([[0,1], [1,0]])
A_exchangeRows = np.matmul(per1, A)
print(A_exchangeRows)

# exchange columns 1 and 2:
A_exchangeColumns = np.matmul(A, per1)
print(A_exchangeColumns)
