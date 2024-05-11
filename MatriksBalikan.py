import numpy as np

def inverseMatrix(a):
    # Calculate the inverse of matrix a using numpy's built-in function
    a_inverse = np.linalg.inv(a)
    return a_inverse

def solveWithInverse(a, b):
    # Calculate the inverse of matrix a
    a_inverse = inverseMatrix(a)
    
    # Calculate the solution by multiplying the inverse of A with b
    x = np.dot(a_inverse, b)
    
    return x

# Initial coefficient matrix
a = np.array([[1.0, 1.0, 1.0], [1.0, -1.0, -1.0], [1.0, -2.0, 3.0]])
# Constant vector
b = np.array([1.0, 1.0, -5.0])

print("Matriks koefisien A:")
print(a)

print("\nVektor konstanta b:")
print(b)

# Copy the original coefficient matrix and constant vector
aOrig = a.copy()
bOrig = b.copy()

# Solve the system using inverse matrix method
x = solveWithInverse(a, b)

print("\nMetode Matriks Balikan:")
print("Solution x:")
print(x)

# Check result: [a]{x} - b
print("\nCheck result: Ax =\n", np.dot(aOrig, x))

# Check if the result of [a]{x} is equal to b
if np.allclose(np.dot(aOrig, x), bOrig):
    print("Verifikasi berhasil: Ax=B")
else:
    print("Verifikasi gagal: Ax tidak sama dengan B")