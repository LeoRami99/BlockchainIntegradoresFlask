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
            rol = request.form['rol']
            # ciclo = request.form['ciclo']
            # print(id_usuario, " ", rol, " ", ciclo)
            sql_actualizar = """UPDATE projecto_usuario SET rol_id_id = %s WHERE id = %s"""
            cursor.execute(sql_actualizar, (rol, id_usuario))
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
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s  WHERE ciclo = %s and grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, ciclo, grupo))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "2":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s  WHERE ciclo = %s and grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, ciclo, grupo))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "3":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            jurado_tres = request.form['jurado_tres']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s  WHERE ciclo = %s and grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, ciclo, grupo))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "4":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            jurado_tres = request.form['jurado_tres']
            jurado_cuatro = request.form['jurado_cuatro']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s  WHERE ciclo = %s and grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, ciclo, grupo))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "5":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            jurado_tres = request.form['jurado_tres']
            jurado_cuatro = request.form['jurado_cuatro']
            jurado_cinco = request.form['jurado_cinco']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s  WHERE ciclo = %s and grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, ciclo, grupo))
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
        sql_consulta_jurados = """SELECT id_jurado_ciclo FROM projecto_juradosciclo WHERE ciclo = %s and grupo_ciclo=%s"""
        cursor.execute(sql_consulta_jurados, (ciclo, grupo))
        jurados = cursor.fetchone()
        grupo=jurados[0]
        sql_actualizar = """UPDATE projecto_proyecto SET jurados_ciclo_id = %s WHERE id_proyecto = %s"""
        cursor.execute(sql_actualizar, (grupo, id_proyecto))
        conn.commit()
        return redirect(url_for('admin.perfiladmin'))

         
