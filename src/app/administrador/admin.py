from flask import Blueprint, render_template, request, redirect, url_for, Response, flash, current_app
from config import *
from flask_mail import Mail, Message
import xlwt
import io
import codecs
from config_eth import *
from flask_login import login_required
conn = EstablecerConexion()
cursor = conn.cursor()
admin= Blueprint('admin',__name__,url_prefix='/admin', template_folder='templates')
def enviar_correo(correo, asunto, ciclo, grupo):
    try:
        with current_app.app_context():
                # Hacer el envio asincrono
            msg = Message(asunto, sender = "fomalhautudecproyectos@gmail.com", recipients = [correo])
                # Correo con estructura HTML
            msg.html = render_template('correoJurado.html', asunto=asunto, ciclo=ciclo, grupo=grupo)
                # Agregar una imagen
            with current_app.open_resource("static/imgs/FomalHauticon.png") as fp:
                msg.attach("FomalHauticon.png", "image/png", fp.read(), 'inline', headers=[('Content-ID', '<image1>')])
            mail=Mail(current_app)
            mail.send(msg)
    except Exception as e:
        flash("Error al enviar el correo, codigo de error: {}".format(e))
@admin.route('/perfiladmin')
@login_required
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
            flash('Datos actualizados correctamente')
            return redirect(url_for('admin.perfiladmin'))
        except:
            return "Error al actualizar"
@login_required
@admin.route("/eliminar/<id>" , methods=['GET'])
def eliminar(id):
    if request.method == 'GET':
        try:
            sql_eliminar = """DELETE FROM projecto_usuario WHERE id = {}""".format(id)
            cursor.execute(sql_eliminar)
            conn.commit()
            flash('Profesor eliminado correctamente')
            return redirect(url_for('admin.perfiladmin'))
        except:
            return "Error al eliminar"
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
            # Enviar un correo al jurado uno
            correo_jurado_uno = get_correo_jurado(jurado_uno)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_uno, asunto, ciclo, grupo)
            flash('Jurados actualizados correctamente')
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "2":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s, numero_jurados = %s WHERE ciclo = %s AND grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, num_jurados, ciclo, grupo))
            conn.commit()
            # Enviar un correo al jurado uno
            correo_jurado_uno = get_correo_jurado(jurado_uno)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_uno, asunto, ciclo, grupo)
            # Enviar un correo al jurado dos
            correo_jurado_dos = get_correo_jurado(jurado_dos)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_dos, asunto, ciclo, grupo)
            flash('Jurados actualizados correctamente')
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "3":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            jurado_tres = request.form['jurado_tres']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s, numero_jurados = %s WHERE ciclo = %s AND grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, num_jurados, ciclo, grupo))
            conn.commit()
            # Enviar un correo al jurado uno
            correo_jurado_uno = get_correo_jurado(jurado_uno)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_uno, asunto, ciclo, grupo)
            # Enviar un correo al jurado dos
            correo_jurado_dos = get_correo_jurado(jurado_dos)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_dos, asunto, ciclo, grupo)
            # Enviar un correo al jurado tres
            correo_jurado_tres = get_correo_jurado(jurado_tres)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_tres, asunto, ciclo, grupo)
            flash('Jurados actualizados correctamente')
            return redirect(url_for('admin.perfiladmin'))
        elif num_jurados == "4":
            jurado_uno = request.form['jurado_uno']
            jurado_dos = request.form['jurado_dos']
            jurado_tres = request.form['jurado_tres']
            jurado_cuatro = request.form['jurado_cuatro']
            sql_actualizar = """UPDATE projecto_juradosciclo SET id_jurado_uno_id = %s, id_jurado_dos_id = %s, id_jurado_tres_id = %s, id_jurado_cuatro_id = %s, id_jurado_cinco_id = %s, numero_jurados = %s WHERE ciclo = %s AND grupo_ciclo=%s"""
            cursor.execute(sql_actualizar, (jurado_uno, jurado_dos, jurado_tres, jurado_cuatro, jurado_cinco, num_jurados, ciclo, grupo))
            conn.commit()
            # Enviar un correo al jurado uno
            correo_jurado_uno = get_correo_jurado(jurado_uno)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_uno, asunto, ciclo, grupo)
            # Enviar un correo al jurado dos
            correo_jurado_dos = get_correo_jurado(jurado_dos)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_dos, asunto, ciclo, grupo)
            # Enviar un correo al jurado tres
            correo_jurado_tres = get_correo_jurado(jurado_tres)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_tres, asunto, ciclo, grupo)
            # Enviar un correo al jurado cuatro
            correo_jurado_cuatro = get_correo_jurado(jurado_cuatro)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_cuatro, asunto, ciclo, grupo)
            flash('Jurados actualizados correctamente')
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
            # Enviar un correo al jurado uno
            correo_jurado_uno = get_correo_jurado(jurado_uno)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_uno, asunto, ciclo, grupo)
            # Enviar un correo al jurado dos
            correo_jurado_dos = get_correo_jurado(jurado_dos)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_dos, asunto, ciclo, grupo)
            # Enviar un correo al jurado tres
            correo_jurado_tres = get_correo_jurado(jurado_tres)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_tres, asunto, ciclo, grupo)
            # Enviar un correo al jurado cuatro
            correo_jurado_cuatro = get_correo_jurado(jurado_cuatro)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_cuatro, asunto, ciclo, grupo)
            # Enviar un correo al jurado cinco
            correo_jurado_cinco = get_correo_jurado(jurado_cinco)
            asunto = "Asignación de jurado"
            enviar_correo(correo_jurado_cinco, asunto, ciclo, grupo)
            flash('Jurados actualizados correctamente')
            return redirect(url_for('admin.perfiladmin'))
        else:
            return "Error al actualizar"
def get_correo_jurado(id):
    sql = """SELECT correo FROM projecto_usuario WHERE id = {}""".format(id)
    cursor.execute(sql)
    correo = cursor.fetchone()
    return correo[0]

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

        sql_actualizar = """UPDATE projecto_proyecto SET jurados_ciclo_id = %s, num_jurados = %s WHERE id_proyecto = %s"""
        cursor.execute(sql_actualizar, (grupo, num_jurados, id_proyecto))
        conn.commit()
        flash('Proyecto asignado correctamente')
        return redirect(url_for('admin.perfiladmin'))
    else:
        flash('Error al asignar proyecto')
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
        flash('Fechas actualizadas correctamente')
        return redirect(url_for('admin.perfiladmin'))
@admin.route("/reporte/ciclo1")
def reporte_ciclo1():
    w3 = conection_eth()
    calif_obser=[]
    sql_proyectos = "SELECT * FROM projecto_proyecto"
    cursor.execute(sql_proyectos)
    proyectos = cursor.fetchall()

    # Traer las calificaciones del usuario
    for proyects in proyectos:
        sql_calificaciones = "SELECT * FROM projecto_calificaciones WHERE id_proyecto_id = '{0}'".format(proyects[0])
        cursor.execute(sql_calificaciones)
        calificaciones = cursor.fetchall()
        for calif in calificaciones:
            if proyects[11] == 1:
                if calif[3] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_uno=bytes.fromhex(nota_1[2:]).decode('utf-8')
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_uno,proyects[3]])
            elif proyects[11] == 2:
                if calif[3] == None or calif[4] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos)) / 2
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
            elif proyects[11] == 3:
                if calif[3] == None or calif[4] == None or calif[5] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_tres = bytes.fromhex(nota_3[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos) + float(nota_tres)) / 3
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
                    
            elif proyects[11] == 4:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_tres = bytes.fromhex(nota_3[2:]).decode('utf-8')
                    nota_cuatro = bytes.fromhex(nota_4[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos) + float(nota_tres) + float(nota_cuatro)) / 4
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
            elif proyects[11] == 5:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None or calif[7] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    nota_5=w3.eth.getTransaction(calif[7]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_tres = bytes.fromhex(nota_3[2:]).decode('utf-8')
                    nota_cuatro = bytes.fromhex(nota_4[2:]).decode('utf-8')
                    nota_cinco = bytes.fromhex(nota_5[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos) + float(nota_tres) + float(nota_cuatro) + float(nota_cinco)) / 5
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
    # Generar el reporte en excel
    # Creamos el libro de trabajo
    salida = io.BytesIO()
    libro = xlwt.Workbook()
    hoja=libro.add_sheet("Reporte Ciclo I")
    # Headers
    hoja.write(0, 0, "ID")
    hoja.write(0, 1, "Nombre")
    hoja.write(0, 2, "Ciclo")
    hoja.write(0, 3, "Fecha Entrega")
    hoja.write(0, 4, "Estudiante 1")
    hoja.write(0, 5, "Estudiante 2")
    hoja.write(0, 6, "Estudiante 3")
    hoja.write(0, 7, "Calificación")

    idx=0
    for row in calif_obser:
        if row[3] == '1':
            idx+=1
            hoja.write(idx, 0, row[1])
            hoja.write(idx, 1, row[2])
            hoja.write(idx, 2, row[3])
            hoja.write(idx, 3, formato_fecha(row[10]))
            hoja.write(idx, 4, row[4])
            hoja.write(idx, 5, row[5])
            hoja.write(idx, 6, row[6])
            hoja.write(idx, 7, row[9])
    libro.save(salida)
    salida.seek(0)
    return Response(salida, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=reporte_ciclo1.xls"})
def get_usuario_doc(id_user):
    id_usuario=str(id_user)
    sql_usuari = "SELECT * FROM projecto_usuario WHERE id = {0}".format(id_usuario)
    cursor.execute(sql_usuari)
    usuario = cursor.fetchone()
    return usuario[4]
@admin.route("/reporte/ciclo2")
def reporte_ciclo2():
    w3 = conection_eth()
    calif_obser=[]
    sql_proyectos = "SELECT * FROM projecto_proyecto"
    cursor.execute(sql_proyectos)
    proyectos = cursor.fetchall()

    # Traer las calificaciones del usuario
    for proyects in proyectos:
        sql_calificaciones = "SELECT * FROM projecto_calificaciones WHERE id_proyecto_id = '{0}'".format(proyects[0])
        cursor.execute(sql_calificaciones)
        calificaciones = cursor.fetchall()
        for calif in calificaciones:
            if proyects[11] == 1:
                if calif[3] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_1,proyects[3]])
            elif proyects[11] == 2:
                if calif[3] == None or calif[4] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos)) / 2
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
            elif proyects[11] == 3:
                if calif[3] == None or calif[4] == None or calif[5] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_tres = bytes.fromhex(nota_3[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos) + float(nota_tres)) / 3
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
                    
            elif proyects[11] == 4:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_tres = bytes.fromhex(nota_3[2:]).decode('utf-8')
                    nota_cuatro = bytes.fromhex(nota_4[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos) + float(nota_tres) + float(nota_cuatro)) / 4
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
            elif proyects[11] == 5:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None or calif[7] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    nota_5=w3.eth.getTransaction(calif[7]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_tres = bytes.fromhex(nota_3[2:]).decode('utf-8')
                    nota_cuatro = bytes.fromhex(nota_4[2:]).decode('utf-8')
                    nota_cinco = bytes.fromhex(nota_5[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos) + float(nota_tres) + float(nota_cuatro) + float(nota_cinco)) / 5
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
    # Generar el reporte en excel
    # Creamos el libro de trabajo
    salida = io.BytesIO()
    libro = xlwt.Workbook()
    hoja=libro.add_sheet("Reporte Ciclo I")
    # Headers
    hoja.write(0, 0, "ID")
    hoja.write(0, 1, "Nombre")
    hoja.write(0, 2, "Ciclo")
    hoja.write(0, 3, "Fecha Entrega")
    hoja.write(0, 4, "Estudiante 1")
    hoja.write(0, 5, "Estudiante 2")
    hoja.write(0, 6, "Estudiante 3")
    hoja.write(0, 7, "Calificación")

    idx=0
    for row in calif_obser:
        if row[3] == '2':
            idx+=1
            hoja.write(idx, 0, row[1])
            hoja.write(idx, 1, row[2])
            hoja.write(idx, 2, row[3])
            hoja.write(idx, 3, formato_fecha(row[10]))
            hoja.write(idx, 4, row[4])
            hoja.write(idx, 5, row[5])
            hoja.write(idx, 6, row[6])
            hoja.write(idx, 7, row[9])
    libro.save(salida)
    salida.seek(0)
    return Response(salida, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=reporte_ciclo2.xls"})
@admin.route("/reporte/ciclo3")
def reporte_ciclo3():
    w3 = conection_eth()
    calif_obser=[]
    sql_proyectos = "SELECT * FROM projecto_proyecto"
    cursor.execute(sql_proyectos)
    proyectos = cursor.fetchall()

    # Traer las calificaciones del usuario
    for proyects in proyectos:
        sql_calificaciones = "SELECT * FROM projecto_calificaciones WHERE id_proyecto_id = '{0}'".format(proyects[0])
        cursor.execute(sql_calificaciones)
        calificaciones = cursor.fetchall()
        for calif in calificaciones:
            if proyects[11] == 1:
                if calif[3] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_1,proyects[3]])
            elif proyects[11] == 2:
                if calif[3] == None or calif[4] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos)) / 2
                    nota_final = "{:.2f}".format(nota_final)
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
            elif proyects[11] == 3:
                if calif[3] == None or calif[4] == None or calif[5] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_tres = bytes.fromhex(nota_3[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos) + float(nota_tres)) / 3
                    nota_final = "{:.2f}".format(nota_final)
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
                    
            elif proyects[11] == 4:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_tres = bytes.fromhex(nota_3[2:]).decode('utf-8')
                    nota_cuatro = bytes.fromhex(nota_4[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos) + float(nota_tres) + float(nota_cuatro)) / 4
                    # aplicar formato decimal a la nota
                    nota_final = "{:.2f}".format(nota_final)
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
            elif proyects[11] == 5:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None or calif[7] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    nota_5=w3.eth.getTransaction(calif[7]).input
                    # convertir de hexadecimal a string
                    nota_uno = bytes.fromhex(nota_1[2:]).decode('utf-8')
                    nota_dos = bytes.fromhex(nota_2[2:]).decode('utf-8')
                    nota_tres = bytes.fromhex(nota_3[2:]).decode('utf-8')
                    nota_cuatro = bytes.fromhex(nota_4[2:]).decode('utf-8')
                    nota_cinco = bytes.fromhex(nota_5[2:]).decode('utf-8')
                    nota_final= (float(nota_uno) + float(nota_dos) + float(nota_tres) + float(nota_cuatro) + float(nota_cinco)) / 5
                    nota_final = "{:.2f}".format(nota_final)
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_final,proyects[3]])
    # Generar el reporte en excel
    # Creamos el libro de trabajo
    salida = io.BytesIO()
    libro = xlwt.Workbook()
    hoja=libro.add_sheet("Reporte Ciclo I")
    # Headers
    hoja.write(0, 0, "ID")
    hoja.write(0, 1, "Nombre")
    hoja.write(0, 2, "Ciclo")
    hoja.write(0, 3, "Fecha Entrega")
    hoja.write(0, 4, "Estudiante 1")
    hoja.write(0, 5, "Estudiante 2")
    hoja.write(0, 6, "Estudiante 3")
    hoja.write(0, 7, "Calificación")

    idx=0
    for row in calif_obser:
        if row[3] == '3':
            idx+=1
            hoja.write(idx, 0, row[1])
            hoja.write(idx, 1, row[2])
            hoja.write(idx, 2, row[3])
            hoja.write(idx, 3, formato_fecha(row[10]))
            hoja.write(idx, 4, row[4])
            hoja.write(idx, 5, row[5])
            hoja.write(idx, 6, row[6])
            hoja.write(idx, 7, row[9])
    libro.save(salida)
    salida.seek(0)
    return Response(salida, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=reporte_ciclo3.xls"})

def obtener_num_doc(id):
    sql_consulta = """SELECT doc_identidad FROM projecto_usuario WHERE id = {}""".format(id)
    cursor.execute(sql_consulta)
    num_doc = cursor.fetchone()
    return num_doc[0]
def formato_fecha(fecha):
    return fecha.strftime("%d/%m/%Y")


         
