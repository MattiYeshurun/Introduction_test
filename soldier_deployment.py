import sqlite3

conn = sqlite3.connect("database.db")

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS soldiers_deployment( 
            id INT NOT NULL PRIMARY KEY, 
            first_name TEXT NOT NULL, 
            last_name TEXT NOT NULL, 
            gender TEXT NOT NULL, 
            city TEXT NOT NULL, 
            distance_in_km INTEGER NOT NULL,
            is_assigned BOOL NOT NULL);
             """)

conn.commit()


load_data = cur.execute("SELECT * FROM `hayal_300_no_status` WHERE id_number >= 8000000 ORDER by distance_in_km DESC LIMIT 160;")



