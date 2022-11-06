from config import *

conn = EstablecerConexion()
cursor = conn.cursor()
class Proyectos():
    def __init__(self, nombre_proyecto, ciclo, estudiante_uno, estudiante_dos, estudiante_tres, jurado_ciclo, fecha_hora_entrega, hash_proyecto, hash_anexos, estado):
        self.nombre = nombre_proyecto
        self.ciclo = ciclo
        self.estudiante_uno = estudiante_uno
        self.estudiante_dos = estudiante_dos
        self.estudiante_tres = estudiante_tres
        self.jurado_ciclo = jurado_ciclo
        self.fecha_hora_entrega = fecha_hora_entrega
        self.hash_proyecto = hash_proyecto
        self.hash_anexos = hash_anexos
        self.estado = estado
    
    def set_proyecto(self):
        # proyecto = Proyecto(nombre_proyecto=self.nombre, ciclo=self.ciclo, estudiante_uno=self.estudiante_uno, estudiante_dos=self.estudiante_dos, estudiante_tres=self.estudiante_tres, jurado_ciclo=self.jurado_ciclo, fecha_hora_entrega=self.fecha_hora_entrega, hash_proyecto=self.hash_proyecto, hash_anexos=self.hash_anexos)
        sql="INSERT INTO projecto_proyecto (nombre_proyecto, ciclo, fecha_hora_entrega, id_hash_documento, id_hash_anexos, estudiante_dos_id, estudiante_tres_id, estudiante_uno_id, jurados_ciclo_id, estado_calificado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.nombre, self.ciclo, self.fecha_hora_entrega, self.hash_proyecto, self.hash_anexos, self.estudiante_uno, self.estudiante_dos, self.estudiante_tres, self.jurado_ciclo, self.estado))
        conn.commit()
def get_proyectos():
    sql="SELECT * FROM projecto_proyecto"
    cursor.execute(sql)
    proyectos = cursor.fetchall()
    return proyectos