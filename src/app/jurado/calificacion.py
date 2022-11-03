from config import *
conn = EstablecerConexion()
cursor = conn.cursor()
class Calificacion():
    def __init__(self, calificacion, observaciones, fecha, id_proyecto, id_jurado):
        self.calificacion = calificacion
        self.observaciones = observaciones
        self.fecha = fecha 
        self.id_proyecto = id_proyecto
        self.id_jurado = id_jurado
    def set_calificaciones(self):
        sql = "INSERT INTO projecto_calificaciones (calificacion, observaciones, fecha, id_proyecto_id, id_usuario_id) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (self.calificacion, self.observaciones, self.fecha, self.id_proyecto, self.id_jurado))
        conn.commit()
        

