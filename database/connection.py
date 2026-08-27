import sqlite3 

DB_NAME = "Linear_system.db" # file

def get_connection():
	# Open and return connection in data base
	return sqlite3.connect(DB_NAME)
	
def init_db():
    # Create table if not exists
    conn = get_connection()
    cursor = conn.cursor()

    # Main table for metadata

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Systems (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_project TEXT NOT NULL,
    size INTEGER NOT NULL,
    solve_method TEXT NOT NULL,
    date_calcul TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
                   """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Coefficient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    system_id INTEGER NOT NULL,
    rows INTEGER NOT NULL,
    columns INTEGER NOT NULL,
    A_value REAL NOT NULL,
    B_value REAL NOT NULL,
    FOREIGN KEY(system_id) REFERENCES Systems(id)
     );
    """)
    
    # Table to store X result
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Solution ( 
    system_id INTEGER PRIMARY KEY,
    X_vector TEXT NOT NULL,
    calculus_time REAL NOT NULL,
    FOREIGN KEY(system_id) REFERENCES Systems(id)
     );
    """)
    
    conn.commit() # To save
    conn.close()
