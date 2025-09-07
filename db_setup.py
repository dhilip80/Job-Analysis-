import sqlite3
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer (
    cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cust_name TEXT NOT NULL,
    cust_mobile TEXT UNIQUE NOT NULL,
    cust_email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    status CHAR(1) DEFAULT 'A'
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS admin (
    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')
cursor.execute("INSERT OR IGNORE INTO admin (username, password) VALUES (?, ?)", ("admin", "admin"))

conn.commit()
conn.close()

print("Database setup completed successfully!")

