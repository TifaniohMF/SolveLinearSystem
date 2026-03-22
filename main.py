import numpy as np
from decomposition.lu import decomposition_lu
from decomposition.qr import decomposition_qr
from decomposition.cholesky import decomposition_cholesky
from solver import solve_system

def solve_linear_system(A, b, method='LU'):
    '''Solve system to use method choice'''
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    print(f"\n ===== SOLVE BY METHOD {method} ===== \n")

    if method == 'LU':
        # Ax = b => LUx = b. We solve Ly = b then Ux = y
        L, U = decomposition_lu(A)
        x = solve_system(L, U, b, kind='LU')

    elif method == 'Cholesky':
        # Ax = b => LL^T x = b. We solve Ly = b then l^T x = y
        L = decomposition_cholesky(A)
        x = solve_system(L,L.T, b, kind='Cholesy')

    elif method == 'QR':
        # Ax = b => QRx = b => Rx = Q^T b
        Q, R = decomposition_qr(A)
        y = np.dot(Q.T, b)
        x = solve_system(None, R, y, kind='QR')
    else:
        raise ValueError("Unrecognized method")
    
    return x

# ======= Exemple to use =======
if __name__ == '__main__':
    A_test = [[1,1,2],
              [1,0,0],
              [2,0,2]]
    
    b_test = [1, 1, 1]

    try:
        solution = solve_linear_system(A_test, b_test, method='QR')
        print(f"x solution : {solution}")

        # Verify
        verify = np.allclose(np.dot(A_test, solution), b_test)
        print(f"Verify (Ax = b): {'success' if verify else 'Echec'}")
    except Exception as e:
        print(f"Error : {e}")
