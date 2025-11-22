import psycopg2


def get_connection(psw):
    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="postgres",
        user="postgres",
        password= psw
    )
