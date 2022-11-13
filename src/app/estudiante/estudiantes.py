from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, session
# from web3 import Web3
from flask_login import login_required
import ipfshttpclient
from .proyecto import Proyectos
from config import *
from config_eth import *
conn = EstablecerConexion()
cursor = conn.cursor()
estudiantes= Blueprint('estudiantes',__name__,url_prefix='/estudiantes', template_folder='templates')

        
        
@estudiantes.route('/registroproyecto')
@login_required
def registroproyecto():
    return render_template("registroProyecto.html")
@estudiantes.route('/registroproyecto_segunda_entrega')
@login_required
def registroproyecto_segunda():
    return render_template("registroProyectoDos.html")

@estudiantes.route('/registrar_proyecto', methods=['POST'])
def registrar_proyecto():
    # Instancia de la conexión a IPFS
    fs = ipfshttpclient.connect('/ip4/192.168.0.15/tcp/5001')
    # Instancia de web3 para envio de transacción a blockchain
    w3 = conection_eth()
    
    # Variables para guardar los integrantes del equipo
    if request.method == 'POST':

        integrante_dos='1'
        integrante_tres='1'
        entrega=request.form['entrega']
        ciclo = request.form['ciclo']
        n_integrantes = request.form['numero_miembros']
        integrante_uno = get_user(request.form['integrante_1'])
        if n_integrantes == '2':
            integrante_dos = get_user(request.form['integrante_2'])
            integrante_tres = '1'
        elif n_integrantes == '3':
            integrante_dos = get_user(request.form['integrante_2'])
            integrante_tres = get_user(request.form['integrante_3'])
        nombrep = request.form['nombrep']
        doc_proyecto = request.files['docfile']
        # Se capturan los datos del documento
        doc_anexos = request.files['anexos_proyecto']
        doc_proyecto.name = nombrep + ".pdf"
        up_projecto_file = fs.add(doc_proyecto)
        hash_ipfs_projecto=up_projecto_file.get('Hash')
        data_projecto=w3.toHex(text=hash_ipfs_projecto)
        tx_projecto={
            'from': "0xbB98661629e0d9263F527acB44084BFDB0d9b86c",
            'value': 0,
            'gas': 2000000,
            'gasPrice': w3.toWei('1', 'gwei'),
            'data': data_projecto
        }
        tx_send_trans_proyecto = w3.eth.sendTransaction(tx_projecto)
        hash_trans_proyecto = tx_send_trans_proyecto.hex()
        
        if doc_anexos.filename == '':
            hash_trans_anexos = 'Sin anexos'
        else:
        # Se cambia el nombre del documento dependiendo del nombre del proyecto
            doc_anexos.name = nombrep + "_anexos.pdf"
            # Se guarda el documento en IPFS
            up_anexos_file = fs.add(doc_anexos)
            # Se guarda el hash en variables para parcealas a hexadecimal para subir a la blockchain
            hash_ipfs_anexos=up_anexos_file.get('Hash')
            # Se convierte el hash a hexadecimal
            data_anexos=w3.toHex(text=hash_ipfs_anexos)
            tx_anexos={
                'from': "0xbB98661629e0d9263F527acB44084BFDB0d9b86c",
                'value': 0,
                'gas': 2000000,
                'gasPrice': w3.toWei('1', 'gwei'),
                'data': data_anexos
            }
            # se envia la transacciones 
            tx_send_trans_anexos = w3.eth.sendTransaction(tx_anexos)
            # Se obtiene el hash de la transacción para cada documento
            hash_trans_anexos = tx_send_trans_anexos.hex()
        
        fecha_hora = datetime.now() 
        #Generar fecha y hora
        
        # Se guarda el proyecto en la base de datos
        proyecto = Proyectos(nombrep, ciclo, integrante_dos, integrante_tres, integrante_uno, 11, fecha_hora, hash_trans_proyecto, hash_trans_anexos, 'false', entrega)
        proyecto.set_proyecto()
        # obtener el id del proyecto
        return redirect(url_for('estudiantes.perfilestudiante'))
    else:
        return redirect(url_for('estudiantes.registroproyecto'))
def get_user(num_doc):
 
    sql_user = "SELECT * FROM projecto_usuario WHERE doc_identidad = '{0}'".format(num_doc)
    cursor.execute(sql_user)
    id_user = cursor.fetchone()
    if id_user is not None:
        return id_user[0]
    else:
        return None

@estudiantes.route('/perfilestudiante')
@login_required
def perfilestudiante():
    w3 = conection_eth()
    sql_usuario = "SELECT * FROM projecto_usuario"
    cursor.execute(sql_usuario)
    usuarios = cursor.fetchall()
    # Fechas de entregas
    sql_fechas = "SELECT * FROM projecto_parametrosistemas"
    cursor.execute(sql_fechas)
    fechas = cursor.fetchone()
    # fecha de hoy
    fecha_hoy = datetime.now()
    # Aplicar el formato de fecha
    fecha_hoy = fecha_hoy.strftime("%Y-%m-%d")
    # formato de fecha de entrega de proyecto
    fecha_entrega_inicio_e1 = fechas[1].strftime("%Y-%m-%d")
    fecha_entrega_fin_e1 = fechas[2].strftime("%Y-%m-%d")
    fecha_entrega_inicio_e2 = fechas[3].strftime("%Y-%m-%d")
    fecha_entrega_fin_e2 = fechas[4].strftime("%Y-%m-%d")
    if fecha_hoy >= fecha_entrega_inicio_e1 and fecha_hoy <= fecha_entrega_fin_e1:
        estado_entrega_e1 = True
    else:
        estado_entrega_e1 = False
    if fecha_hoy > fecha_entrega_inicio_e2 and fecha_hoy < fecha_entrega_fin_e2:
        estado_entrega_e2 = True
    else:
        estado_entrega_e2 = False
 
    #    # Traer las ccccccccalifaciones y proyectos del estudiante
    # sql_proyectos = "SELECT id_proyecto, nombre_proyecto, id_hash_documento, id_hash_anexos, estado_calificado, estudiante_uno_id, estudiante_dos_id, estudiante_tres_id FROM projecto_proyecto"
    # sql_calificaciones = "SELECT id_calificacion, fecha id_proyecto_id, id_usuario_id, cali_jurado_uno
    # cursor.execute(sql_proyectos)
    # proyectos = cursor.fetchall()
    # cursor.execute(sql_calificaciones)
    # calificaciones = cursor.fetchall()
    # proyectos_nuevo = []
    # calificaciones_hash = []
    # proyectos_all =[]
    # for todos_proyectos in proyectos:
    #     proyectos_all.append([todos_proyectos[0], todos_proyectos[1], w3.eth.getTransaction(todos_proyectos[2]).input, w3.eth.getTransaction(todos_proyectos[3]).input, todos_proyectos[4], todos_proyectos[5], todos_proyectos[6], todos_proyectos[7]])
    # # for proyecto_l in proyectos:
    # for calificaciones_lista, proyecto_l, todos_proyectos in zip(calificaciones, proyectos, proyectos):
        
    #     if proyecto_l[0] == calificaciones_lista[3]:
    #         # calificaciones_hash.append([calificaciones_lista[0], calificaciones_lista[1], calificaciones_lista[2], calificaciones_lista[3], w3.eth.getTransaction(calificaciones_lista[3]).input])
    #         proyectos_nuevo.append([proyecto_l[0], proyecto_l[1], w3.eth.getTransaction(proyecto_l[2]).input, w3.eth.getTransaction(proyecto_l[3]).input, proyecto_l[4], proyecto_l[5], proyecto_l[6], proyecto_l[7]])
    #         calificaciones_hash.append([calificaciones_lista[0], w3.eth.getTransaction(calificaciones_lista[1]).input, w3.eth.getTransaction(calificaciones_lista[2]).input, proyecto_l[1], proyecto_l[5], proyecto_l[6], proyecto_l[7]]) 
    # return render_template("perfilEstudiante.html", proyectos=proyectos_nuevo, calificaciones=calificaciones_hash, allproyectos=proyectos_all)
    return render_template("perfilEstudiante.html", usuarios=usuarios,fecha=fechas, estado_e1=estado_entrega_e1, estado_e2=estado_entrega_e2)
@estudiantes.route("/actualizar" , methods=['POST'])
def actualizar():
    if request.method == 'POST':
        try:
            id_usuario = request.form['id_modificar']
            nombre = request.form['nombres']
            apellidos = request.form['apellidos']
            correo = request.form['correo']
            doc_identidad = request.form['n_documento']
            tipo_doc = request.form['tip_doc']
            # ciclo = request.form['ciclo']
            # print(id_usuario, " ", rol, " ", ciclo)
            sql_update = "UPDATE projecto_usuario SET nombre = '{0}', apellidos = '{1}', correo = '{2}', doc_identidad = '{3}', tipo_documento_id= '{4}' WHERE id = '{5}'".format(nombre, apellidos, correo, doc_identidad, tipo_doc, id_usuario)
            cursor.execute(sql_update)
            conn.commit()
            return redirect(url_for('estudiantes.perfilestudiante'))
        except:
            return redirect(url_for('estudiantes.perfilestudiante'))


