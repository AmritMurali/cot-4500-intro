import numpy as np

def printArray(ar):
  for j in range(ar.shape[0]):
    for k in range(ar.shape[1]):
      print(int(ar[j][k]), end=" ")
    print()


mat = np.zeros((3, 3))
for i in range(3):
  mat[i][i] = 1

printArray(mat)

for a in range(3):
  for b in range(3):
    if (a != b):
      mat[a][b] = 3

print()
printArray(mat)

mat = np.delete(mat, 2, 1)  # delete second column of C

print()
printArray(mat)