import numpy as np

def solve_system(L, U, b, kind='LU'):
    ''' Manages the descent and ascent according to the method '''
    # 1. Descent (Forward substitution) for Ly = b
    
    if kind in ['LU','Cholesky']:
        y = np.zeros_like(b, dtype=float)
        for i in range(len(b)):
            y[i] = (b[i] - np.dot(L[i,:i],y[:i])) / L[i,i]

    else : # For QR, b is already trasformed in Q^T * b
        y = b

    # Ascent (Forward substitution) for Ux = y
    x = np.zeros_like(y)
    n =len(y)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:]))/ U[i,i]
    return x