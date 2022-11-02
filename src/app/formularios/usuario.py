
from config import *

conn = EstablecerConexion()
cursor = conn.cursor()
class Usuarios():
    def __init__(self, nombre, apellidos, correo, doc_identidad, cod_universidad, contrasena, ciclo, rol_id, tipo_documento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.tipo_documento = tipo_documento
        self.doc_identidad = doc_identidad
        self.cod_universidad = cod_universidad
        self.contrasena = contrasena
        self.rol_id = rol_id
        self.ciclo = ciclo
    def set_usuario(self):
        # el id es autoincremental
        sql="INSERT INTO projecto_usuario (nombre, apellidos, correo, doc_identidad, cod_universidad, contrasena, ciclo, rol_id_id, tipo_documento_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.nombre, self.apellidos, self.correo, self.doc_identidad, self.cod_universidad, self.contrasena, self.ciclo, self.rol_id, self.tipo_documento))
        conn.commit()

def get_usuarios():
    sql="SELECT * FROM projecto_usuario "
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    return usuarios