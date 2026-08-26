import time
import numpy as np
from decomposition.lu import decomposition_lu
from decomposition.qr import decomposition_qr
from decomposition.cholesky import decomposition_cholesky
from database.connection import *
from database.repository import save_system, save_solution, system_charged
from solver import solve_system
from diagnostics import build_certificate, validate_system

def solve_linear_system(A, b, method='LU', return_certificate=False):
    '''Solve system to use method choice'''
    A, b = validate_system(A, b)

    print(f"\n ===== SOLVE BY METHOD {method} ===== \n")

    if method == 'LU':
        # Ax = b => LUx = b. We solve Ly = b then Ux = y
        L, U = decomposition_lu(A)
        x = solve_system(L, U, b, kind='LU')

    elif method == 'Cholesky':
        # Ax = b => LL^T x = b. We solve Ly = b then l^T x = y
        L = decomposition_cholesky(A)
        x = solve_system(L, L.T, b, kind='Cholesky')

    elif method == 'QR':
        # Ax = b => QRx = b => Rx = Q^T b
        Q, R = decomposition_qr(A)
        y = np.dot(Q.T, b)
        x = solve_system(None, R, y, kind='QR')
    else:
        raise ValueError("Unrecognized method")
    
    certificate = build_certificate(A, b, x, method)
    if return_certificate:
        return x, certificate
    return x
    
def execute_pipeline():
    print("=== [1] Initial data base ===")
    init_db()
    
    # Data
    # 3x1 + 2x2 = 1
    # 2x1 - 2x2 = -2
    
    A = np.array([[3.0, 2.0], 
                  [2.0, -2.0]])
    B = np.array([1.0, -2.0])
    
    print("\n=== [2] Save the system initial in data base ===")
    id_system = save_system(
        name_project="System test 2×2", 
        A=A, 
        B=B, 
        method="QR method"
    )
    print(f"System registered with ID : {id_system}")
    
    print("\n=== [3] Solve system ===")
    try:
        start_time = time.time()
        X, certificate = solve_linear_system(
            A, B, method='QR', return_certificate=True
        )
        end_time = time.time()
        
        calculus_time = (end_time - start_time) * 1000 # in milliseconds
        print(f"Solution finded: {X}")
        print(f"Calculus time: {calculus_time:.4f} ms")
        print(f"Residual infinity norm: {certificate['residual_norm_inf']:.3e}")
        if certificate['warnings']:
            print(f"Numerical warnings: {', '.join(certificate['warnings'])}")
        
        print("\n=== [4] Save result ===")
        save_solution(id_system, X, calculus_time)
        print("Resultat archived with succes.")
        
    except Exception as e:
        print(f"Error during solving: {e}")

    print("\n=== [Bonus] Verify reading (Reload) ===")
    A_retrieve, B_retrieve = system_charged(id_system)
    print("A matrix recharged since the DB :\n", A_retrieve)
    print("B vector recharged since the DB :", B_retrieve)

if __name__ == "__main__":
    execute_pipeline()