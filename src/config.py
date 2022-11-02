from psycopg2 import connect

HOST = 'localhost'
PORT = 5432
BD = 'fomalhaut'
USUARIO = 'postgres'
PASSWORD = ''

def EstablecerConexion():
    try:
        conexion = connect(host=HOST, port=PORT, dbname=BD, user=USUARIO, password=PASSWORD)
    except ConnectionError:
        print("conexion fallida")
    return conexion