from db import get_connection


password = str(input("Database Password: "))


try:
    conn = get_connection(password)
    print("Database connection successful")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
