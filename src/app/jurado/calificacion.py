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
        
    def set_calificacion_observacion_jurado_uno(self):
        try:
            cursor.execute("UPDATE calificacion SET calificacion = %s, observaciones = %s, nota_jurado = %s WHERE id_proyecto = %s AND id_jurado = %s", (self.calificacion, self.observaciones, self.nota_jurado, self.id_proyecto, self.id_jurado))
            conn.commit()
            return True
        except:
            return False
        
        
def get_califaciones(id_proyecto):
    sql = "SELECT * FROM projecto_calificaciones WHERE id_proyecto_id = {}".format(id_proyecto)
    cursor.execute(sql)
    calificaciones = cursor.fetchall()
    return calificaciones

