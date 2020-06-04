import math
import numpy as np
import pandas as pd
num_list = [4, 2, 7, 9, 3, 5, 2, 3 , 9, 0, 6]

sum_list = sum(num_list)
print(f'1. The sum of the list is {sum_list}')

max_list = max(num_list)
print(f'2. The largest number is {max_list}')

min_list = min(num_list)
print(f'3. The smallest number is {min_list}')

evens = []
for n in num_list:
    if (n % 2) == 0:
        evens.append(n)
print("4. The evens are:\n", evens)

positives = []
for n in num_list:
    if n > 0:
        positives.append(n)
print('5. The positive values are:\n', positives)

uniq_pos = set(positives)
print('6. The unique positive values are:\n', uniq_pos)

factor = int(input('Number to multiply by? '))

print('7. The multiplied list is:\n', np.array(num_list)*factor)

array1 = np.array([2,4,5])
array2 = np.array([2,3,6])

print("8. The multiplied arrays equal:\n", array1*array2)

array3 = np.array([[1,3],[2,4]])
array4 = np.array([[5,2],[1,0]])

print('9. The added matrixes equal:\n', array3+array4)

print('\n10. For any two arrays A1 and A2 of m*n size,\n sum = zeros(len(A1)[0],len(A1)[1])\n for i in range(0,len(A1)[0]):\n   for n in range(0,len(A1)[1]):\n       sum(i,n) = A1(i,n) + A2(i,n)\n')

de_dup = []

for n in num_list:
    if n not in de_dup:
        de_dup.append(n)

print(de_dup)

ar3 = pd.DataFrame(array3)
ar4 = pd.DataFrame(array4)
[m, n] = ar3.shape # rows, columns

# by definition, we are multiplying array3 by array 4 as in A*B

m_matrix = np.zeros([m, n])

for i in range(0,m):
    # we need the ith row of A, and the ith column of B
    for t in range(0,n):
        m_matrix[i,t] = ar3.iloc[i,:].dot(ar4.iloc[:,t])

print(m_matrix)

print(ar3.dot(ar4))
