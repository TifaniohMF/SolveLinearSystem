import json
import numpy as np
from database.connection import get_connection

def save_system(name_project, A, B, method):
    # Register the matrix A and B vector. Return ID Generated
    conn = get_connection()
    cursor = conn.cursor()
    n = len(B)

    # Insert into main table
    cursor.execute("INSERT INTO Systems (name_project, size, solve_method) VALUES (?, ?, ?)", (name_project, n, method))

    system_id = cursor.lastrowid

    # Insert the coeff A and B
    for i in range(n):
    	for j in range(n):
        # We register the B value in first colums to avoid duplicate
              val_b = float(B[i]) if j == 0 else 0.0
              cursor.execute("INSERT INTO Coefficient (system_id, rows, columns, A_value, B_value) VALUES (?, ?, ?, ?, ?)", (system_id, i, j, float(A[i, j]), val_b))
    
    conn.commit()
    conn.close()
    return system_id
    
def save_solution(system_id, X, calculus_time):
    # Register the Vector solution
    conn = get_connection()
    cursor = conn.cursor()

    # Conversion table NumPy to chain JSON textual for SQLite
    X_json = json.dumps(X.tolist())
    cursor.execute("INSERT INTO Solution (system_id, X_vector, calculus_time) VALUES (?, ?, ?)", (system_id, X_json, calculus_time))

    conn.commit()
    conn.close()
    
def system_charged(system_id):
	# Retrieve the system stored to can re-use or re-analyzed
	conn = get_connection()
	cursor = conn.cursor()
	
	# Retrieve size
	cursor.execute("SELECT size FROM Systems WHERE id=?", (system_id,))
	sizes = cursor.fetchone()[0]
	
	# Reconstruction A and B
	cursor.execute("SELECT rows, columns, A_value, B_value FROM Coefficient WHERE id=?",(system_id,))
	row = cursor.fetchall()
	
	A = np.zeros((sizes,sizes))
	B = np.zeros(sizes)
	
	for rows, columns, val_a, val_b in row:
		A[rows, columns] = val_a
		if columns == 0:
			B[rows] = val_b
			
	conn.close()
	return A, B
