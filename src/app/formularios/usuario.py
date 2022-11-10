from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from config import *

conn = EstablecerConexion()
cursor = conn.cursor()
class Usuarios():
    def __init__(self, nombre, apellidos, correo, doc_identidad, contrasena, rol_id, tipo_documento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.tipo_documento = tipo_documento
        self.doc_identidad = doc_identidad
        self.contrasena = contrasena
        self.rol_id = rol_id
    def set_usuario(self):
        # el id es autoincremental
        sql="INSERT INTO projecto_usuario (nombre, apellidos, correo, doc_identidad, contrasena, rol_id_id, tipo_documento_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.nombre, self.apellidos, self.correo, self.doc_identidad, generate_password_hash(self.contrasena), self.rol_id, self.tipo_documento))
        conn.commit()

class Usuario(UserMixin):
    def __init__(self,id, correo, contrasena, rol="", nombres="", apellidos=""):
        self.id = id
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        self.nombres = nombres
        self.apellidos = apellidos
    def login(self, conexion):
        cursor = conexion.cursor()
        sql="SELECT * FROM projecto_usuario WHERE correo='{0}' ".format(self.correo)
        cursor.execute(sql)
        fila=cursor.fetchone()
        if fila !=None:
            usuario= Usuario(fila[0], fila[3], check_password_hash(fila[5], self.contrasena), fila[6], fila[1], fila[2])
            return usuario
        else:
            return None
    @classmethod
    def obtener_usuario(self, id):
        cursor = conn.cursor()
        sql="SELECT id, nombre, apellidos, correo, rol_id_id FROM projecto_usuario WHERE id={0}".format(id)
        cursor.execute(sql)
        fila=cursor.fetchone()
        if fila !=None:
            usuario= Usuario(fila[0], fila[3], None, fila[4], fila[1], fila[2])
            return usuario
        else:
            return None
    