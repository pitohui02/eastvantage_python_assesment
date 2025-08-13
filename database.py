import sqlite3

# Database credentials should be on configuration file, this is only for assesment
DB_NAME = "address.db"

# Initialize conn and cursor for reusability
def initialize_conn_and_cursor(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    return conn, cursor

# Initialize database if it does not exist
def initialize_database():
    
    conn, cursor = initialize_conn_and_cursor(DB_NAME)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS address (
                        address_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        label TEXT,
                        address TEXT,
                        latitude REAL NOT NULL,
                        longitude REAL NOT NULL
                    )
                    """)
    
    conn.commit()
    conn.close()
    






    
    
    
    