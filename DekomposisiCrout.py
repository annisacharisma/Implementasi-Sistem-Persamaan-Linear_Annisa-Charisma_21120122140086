import numpy as np

def croutDecomposition(a):
    n = len(a)
    l = np.zeros((n, n))
    u = np.zeros((n, n))
    
    for j in range(n):
        u[j, j] = 1.0
        
        for i in range(j, n):
            sum = 0.0
            for k in range(j):
                sum += l[i, k] * u[k, j]
            l[i, j] = a[i, j] - sum
            
        for i in range(j + 1, n):
            sum = 0.0
            for k in range(j):
                sum += l[j, k] * u[k, i]
            u[j, i] = (a[j, i] - sum) / l[j, j]
            
    return l, u

def solveWithCrout(a, b):
    l, u = croutDecomposition(a)
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)
    
    # Solve Ly = b using forward substitution
    for i in range(n):
        y[i] = b[i] - np.dot(l[i, :i], y[:i])
    
    # Solve Ux = y using backward substitution
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(u[i, i+1:], x[i+1:])) / u[i, i]
    
    return x

# Testing the code
# Initial coefficient matrix
a = np.array([[4.0, 3.0, 2.0], [3.0, 4.0, 1.0], [2.0, 1.0, 3.0]])
# Constant vector
b = np.array([1.0, 2.0, 3.0])

print("Matriks koefisien A:")
print(a)

print("\nVektor konstanta b:")
print(b)

# Solve the system using Crout decomposition method
x = solveWithCrout(a, b)

print("\nMetode Dekomposisi Crout:")
print("Solution x:\n", x)