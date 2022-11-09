from flask import Blueprint, render_template, request, redirect, url_for
from config import *
conn = EstablecerConexion()
cursor = conn.cursor()
admin= Blueprint('admin',__name__,url_prefix='/admin', template_folder='templates')
@admin.route('/perfiladmin')
def perfiladmin():
    sql_rol_admin = """SELECT id, nombre, apellidos, correo, tipo_documento_id, doc_identidad, 
    ciclo, rol_id_id FROM projecto_usuario"""
    cursor.execute(sql_rol_admin)
    rol_admin = cursor.fetchall()
    return render_template("perfilAdministrador.html", profesores=rol_admin)

@admin.route("/actualizar" , methods=['POST'])
def actualizar():
    if request.method == 'POST':
        try:
            id_usuario = request.form['id_modificar']
            rol = request.form['rol']
            ciclo = request.form['ciclo']
            sql_actualizar = """UPDATE projecto_usuario SET rol_id_id = %s, ciclo = %s WHERE id = %s"""
            cursor.execute(sql_actualizar, (rol, ciclo, id_usuario))
            conn.commit()
            return redirect(url_for('admin.perfiladmin'))
        except:
            return "Error al actualizar"

        
