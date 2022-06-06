from random import uniform
from sklearn.preprocessing import StandardScaler
import sys

M = int(4)            # number of rows (samples) in input matrix D
N = int(4)             # number of columns (features) in input matrix
lrange = -100000    # lrange <= element of matrix
urange = 100000     # element of matrix <= urange

# generate the matrix
D = []
for i in range(M):
    temp = []
    for j in range(N):
        temp.append(uniform(lrange, urange))
    D.append(temp)

# standardize
X_std = StandardScaler().fit_transform(D)

filename = 'input.txt'     #output filename
file = open(filename, 'w')

# write size of matrix in first line of file
file.write('%d ' %M)

# write space separated matrix elements
for i in range(M):
    for j in range(N):
        file.write('%.7f ' %(X_std[i][j]))

file.close()