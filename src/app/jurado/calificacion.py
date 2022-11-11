from config import *
conn = EstablecerConexion()
cursor = conn.cursor()
class Calificacion():
    def __init__(self,id_proyecto, id_jurado, nota_jurado1, nota_jurado_2, nota_jurado_3, nota_jurado_4, nota_jurado_5,  observaciones1, observaciones_2, observaciones_3, observaciones_4, observaciones_5): 
        self.id_proyecto = id_proyecto
        self.id_jurado = id_jurado
        self.nota_jurado1 = nota_jurado1
        self.nota_jurado_2 = nota_jurado_2
        self.nota_jurado_3 = nota_jurado_3
        self.nota_jurado_4 = nota_jurado_4
        self.nota_jurado_5 = nota_jurado_5
        self.observaciones1 = observaciones1
        self.observaciones_2 = observaciones_2
        self.observaciones_3 = observaciones_3
        self.observaciones_4 = observaciones_4
        self.observaciones_5 = observaciones_5


        
    def set_calificacion_observacion_jurado_uno(self):
        sql_califacion_uno = "UPDATE projecto_calificaciones SET cali_jurado_uno = %s, obser_jurado_uno = %s WHERE id_proyecto_id = %s"
        cursor.execute(sql_califacion_uno, (self.nota_jurado1, self.observaciones1, self.id_proyecto))
        conn.commit()
    def set_calificacion_observacion_jurado_dos(self):
        sql_califacion_dos = "UPDATE projecto_calificaciones SET cali_jurado_dos = %s, obser_jurado_dos = %s WHERE id_proyecto_id = %s"
        cursor.execute(sql_califacion_dos, (self.nota_jurado_2, self.observaciones_2, self.id_proyecto))
        conn.commit()
    def set_calificacion_observacion_jurado_tres(self):
        sql_califacion_tres = "UPDATE projecto_calificaciones SET cali_jurado_tres = %s, obser_jurado_tres = %s WHERE id_proyecto_id = %s"
        cursor.execute(sql_califacion_tres, (self.nota_jurado_3, self.observaciones_3, self.id_proyecto))
        conn.commit()
    def set_calificacion_observacion_jurado_cuatro(self):
        sql_califacion_cuatro = "UPDATE projecto_calificaciones SET cali_jurado_cuatro = %s, obser_jurado_cuatro = %s WHERE id_proyecto_id = %s"
        cursor.execute(sql_califacion_cuatro, (self.nota_jurado_4, self.observaciones_4, self.id_proyecto))
        conn.commit()
    def set_calificacion_observacion_jurado_cinco(self):
        sql_califacion_cinco = "UPDATE projecto_calificaciones SET cali_jurado_cinco = %s, obser_jurado_cinco = %s WHERE id_proyecto_id = %s"
        cursor.execute(sql_califacion_cinco, (self.nota_jurado_5, self.observaciones_5, self.id_proyecto))
        conn.commit()

        
def get_califaciones(id_proyecto):
    sql = "SELECT * FROM projecto_calificaciones WHERE id_proyecto_id = {}".format(id_proyecto)
    cursor.execute(sql)
    calificaciones = cursor.fetchall()
    return calificaciones

