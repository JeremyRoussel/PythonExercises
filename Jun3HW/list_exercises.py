import math
import numpy as np
import pandas as pd
num_list = [4, 2, 7, 9, 3, 5, 2, 3 , 9, 0, 6]

array1 = np.array([2,4,5])
array2 = np.array([2,3,6])
array3 = np.array([[1,3],[2,4]])
array4 = np.array([[5,2],[1,0]])

def asum():
    sum_list = sum(num_list)
    print(f'1. The sum of the list is {sum_list}')

def amax():
    max_list = max(num_list)
    print(f'2. The largest number is {max_list}')

def amin():
    min_list = min(num_list)
    print(f'3. The smallest number is {min_list}')

def even_nums():
    evens = []
    for n in num_list:
        if (n % 2) == 0:
            evens.append(n)
    print("4. The evens are:\n", evens)

def pos_nums():
    positives = []
    for n in num_list:
        if n > 0:
            positives.append(n)
    print('5. The positive values are:\n', positives)

def uniq_nums():
    uniq_pos = set(positives)
    print('6. The unique positive values are:\n', uniq_pos)

def mult():
    factor = int(input('Number to multiply by? '))
    print('7. The multiplied list is:\n', np.array(num_list)*factor)

def array_mult():
    print("8. The multiplied arrays equal:\n", array1*array2)

def matrix_add():
    print('9. The added matrixes equal:\n', array3+array4)

def how_to_mmult():
    print('''10. For any two arrays A1 and A2 of m*n size,
    sum = zeros(len(A1)[0],len(A1)[1])
    for i in range(0,len(A1)[0]):
        for n in range(0,len(A1)[1]):
            sum(i,n) = A1(i,n) + A2(i,n)''')

def de_dupli():
    de_dup = []
    for n in num_list:
        if n not in de_dup:
            de_dup.append(n)

    print(de_dup)

def mmult():
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

question = ""
questions = {"1":1,"2":2,"3":3,"4":4,"5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "11":11, "12":12}
while question not in questions:
    question = input('''Select a Question:
    1. Sum
    2. Max
    3. Min
    4. Evens
    5. Postitives
    6. Uniques
    7. Mulitply by Scalar
    8. Array Mult
    9. Matrix Addition
    10. How to MMult
    11. De-Dupulicate
    12. Mmult
    ''')
    if questions[question] == 1:
        asum()
        break
    if questions[question] == 2:
        amax()
        break
    if questions[question] == 3:
        amin()
        break
    if questions[question] == 4:
        even_nums()
        break
    if questions[question] == 5:
        pos_nums()
        break
    if questions[question] == 6:
        uniq_nums()
        break
    if questions[question] == 7:
        mult()
        break
    if questions[question] == 8:
        array_mult()
        break
    if questions[question] == 9:
        matrix_add()
        break
    if questions[question] == 10:
        how_to_mmult()
        break
    if questions[question] == 11:
        de_dupli()
        break
    if questions[question] == 12:
        mmult()
        break