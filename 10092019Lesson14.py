#Q1.antisymmetric
# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    temp=[]
    if A == []:
        return True
    if not len(A[0]) == len(A):
        return False
    for i in range(0,len(A[0])):
        t = []
        for j in range(0,len(A[0])):
            t.append(-(A[j][i]))
        temp.append(t)
    if A == temp:
        return True
    else:
        return False
    #Write your code here


# Test Cases:

print(antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]]))
#>>> True

print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]]))
#>>> False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False