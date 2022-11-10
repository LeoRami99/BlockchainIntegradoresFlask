from config import *
conn = EstablecerConexion()
cursor = conn.cursor()
class Calificacion():
    def __init__(self, calificacion, observaciones, fecha, id_proyecto, id_jurado, nota_jurado, nota_jurado_2, nota_jurado_3, nota_jurado_4, nota_jurado_5):
        self.calificacion = calificacion
        self.observaciones = observaciones
        self.fecha = fecha 
        self.id_proyecto = id_proyecto
        self.id_jurado = id_jurado
        self.nota_jurado = nota_jurado
        self.nota_jurado_2 = nota_jurado_2
        self.nota_jurado_3 = nota_jurado_3
        self.nota_jurado_4 = nota_jurado_4
        self.nota_jurado_5 = nota_jurado_5
        
    def set_calificaciones(self):
        sql = "INSERT INTO projecto_calificaciones (calificacion, observaciones, fecha, id_proyecto_id, id_usuario_id) VALUES (%s,%s,%s,%s,%s)"
        sql_update_estado = "UPDATE projecto_proyecto SET estado_calificado = true WHERE id_proyecto = {}".format(self.id_proyecto)
        cursor.execute(sql, (self.calificacion, self.observaciones, self.fecha, self.id_proyecto, self.id_jurado))
        cursor.execute(sql_update_estado)
        conn.commit()
        
def get_califaciones(id_proyecto):
    sql = "SELECT * FROM projecto_calificaciones WHERE id_proyecto_id = {}".format(id_proyecto)
    cursor.execute(sql)
    calificaciones = cursor.fetchall()
    return calificaciones

