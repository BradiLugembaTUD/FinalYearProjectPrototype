import psycopg2

def get_connection(password=None):
    if password is None:
        password = input("Enter PostgreSQL password: ")

    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="postgres",
        user="postgres",
        password=password
    )
