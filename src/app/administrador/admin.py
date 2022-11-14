from flask import Blueprint, render_template, request, redirect, url_for
from config import *
conn = EstablecerConexion()
cursor = conn.cursor()
admin= Blueprint('admin',__name__,url_prefix='/admin', template_folder='templates')
@admin.route('/perfiladmin')
def perfiladmin():
    sql_rol_admin = """SELECT id, nombre, apellidos, correo, tipo_documento_id, doc_identidad, rol_id_id FROM projecto_usuario"""
    cursor.execute(sql_rol_admin)
    rol_admin = cursor.fetchall()
    sql_proyectos= "SELECT id_proyecto, nombre_proyecto, ciclo , jurados_ciclo_id FROM projecto_proyecto"
    cursor.execute(sql_proyectos)
    proyectos = cursor.fetchall()
    return render_template("perfilAdministrador.html", profesores=rol_admin, proyectos=proyectos)

@admin.route("/actualizar" , methods=['POST'])
def actualizar():
    if request.method == 'POST':
        try:
            id_usuario = request.form['id_modificar']
            nombre = request.form['nombres']
            apellidos = request.form['apellidos']
            correo = request.form['correo']
            doc_identidad = request.form['n_documento']
            rol = request.form['rol']
            # ciclo = request.form['ciclo']
            # print(id_usuario, " ", rol, " ", ciclo)
            sql_actualizar = """UPDATE projecto_usuario SET nombre = %s, apellidos = %s, correo = %s, doc_identidad = %s, rol_id_id = %s WHERE id = %s"""
            cursor.execute(sql_actualizar, (nombre, apellidos, correo, doc_identidad, rol, id_usuario))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        except:
            return "Error al actualizar"
@admin.route("/actualizarjurados" , methods=['POST'])
def actualizarjurados():
    if request.method == 'POST':
        ciclo=request.form['ciclo']
        num_jurados = request.form['num_jurados']
        grupo = request.form['grupo']
        jurado_uno="1"
        jurado_dos="1"
        jurado_tres="1"
        jurado_cuatro="1"
        jurado_cinco="1"
        if num_jurados == "1":
            jurado_uno = request.form['jurado_uno']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s, numero_jurados = %s WHERE ciclo = %s AND grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, num_jurados, ciclo, grupo))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "2":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s, numero_jurados = %s WHERE ciclo = %s AND grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, num_jurados, ciclo, grupo))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "3":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            jurado_tres = request.form['jurado_tres']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s, numero_jurados = %s WHERE ciclo = %s AND grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, num_jurados, ciclo, grupo))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "4":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            jurado_tres = request.form['jurado_tres']
            jurado_cuatro = request.form['jurado_cuatro']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s, numero_jurados = %s WHERE ciclo = %s AND grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, num_jurados, ciclo, grupo))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "5":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            jurado_tres = request.form['jurado_tres']
            jurado_cuatro = request.form['jurado_cuatro']
            jurado_cinco = request.form['jurado_cinco']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s  WHERE ciclo = %s and grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, num_jurados, ciclo, grupo))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        else:
            return "Error al actualizar"
@admin.route("/asignargrupo" , methods=['POST'])
def asignargrupo():
    if request.method == 'POST':
        id_proyecto = request.form['id_proyecto']
        ciclo=request.form['ciclo_proyecto']
        grupo = request.form['grupo']
        sql_consulta_jurados = """SELECT id_jurado_ciclo, numero_jurados FROM projecto_juradosciclo WHERE ciclo = %s and grupo_ciclo=%s"""
        cursor.execute(sql_consulta_jurados, (ciclo, grupo))
        jurados = cursor.fetchone()
        grupo=jurados[0]
        num_jurados=jurados[1]

        print("------------------",jurados[1],"------------------")
        sql_actualizar = """UPDATE projecto_proyecto SET jurados_ciclo_id = %s, num_jurados = %s WHERE id_proyecto = %s"""
        cursor.execute(sql_actualizar, (grupo, num_jurados, id_proyecto))
        conn.commit()
        return redirect(url_for('admin.perfiladmin'))
@admin.route("/asignarfechas" , methods=['POST'])
def asignarfechas():
    if request.method == 'POST':
        fecha_inicio_e1 = request.form['fecha_inicio_e1']
        fecha_fin_e1 = request.form['fecha_fin_e1']
        # Fecha de entrega dos
        fecha_inicio_e2 = request.form['fecha_inicio_e2']
        fecha_fin_e2 = request.form['fecha_fin_e2']
        sql_fechas = """UPDATE projecto_parametrosistemas SET fecha_inicio_e1 = %s, fecha_fin_e1 = %s, fecha_inicio_e2 = %s, fecha_fin_e2 = %s WHERE id = 1"""
        cursor.execute(sql_fechas, (fecha_inicio_e1, fecha_fin_e1, fecha_inicio_e2, fecha_fin_e2))
        conn.commit()
        return redirect(url_for('admin.perfiladmin'))

         
