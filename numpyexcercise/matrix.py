import numpy as n

a = n.array([1,2,3])
b = n.array([2,5,7])

sum = a + b

print(f"sum: {sum}")

newb = n.array([[2,5,6], [1,1,1], [1,4,6]])

multiply = a @ newb

print(f"product {multiply}")

rank = n.linalg.matrix_rank(newb)

print(f"rank: {rank}")

print(f"Transpose: {newb.T}")

dist = n.linalg.norm(a)

print(f"distance:{dist}")

print(f"matrix shape: {newb.shape}")

print(f"matrix size: {newb.size}")

print(f"matrix dimension {newb.ndim}")

eigenvalues, eigenvectors = n.linalg.eig(newb)

print(f"eigenvalue:{eigenvalues}")
print(f"eigenvector: {eigenvectors}")