from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
# from web3 import Web3
from flask_login import login_required, current_user
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
        if n_integrantes == '1':
            integrante_dos = '1'
            integrante_tres = '1'
            if verificar_usuario(request.form['integrante_1']):
                integrante_uno = get_user(request.form['integrante_1'])
            else:
                if entrega == '1era Entrega':
                    flash('El integrante 1 no se encuentra registrado en el sistema')
                    return redirect(url_for('estudiantes.registroproyecto'))
                else:
                    flash('El integrante 1 no se encuentra registrado en el sistema')
                    return redirect(url_for('estudiantes.registroproyecto_segunda'))
        elif n_integrantes == '2':
            if verificar_usuario(request.form['integrante_2']):
                integrante_uno = get_user(request.form['integrante_1'])
                integrante_dos = get_user(request.form['integrante_2'])
                integrante_tres = '1'
            else:
                if entrega == '1era Entrega':
                    flash('El integrante 2 no se encuentra registrado en el sistema')
                    return redirect(url_for('estudiantes.registroproyecto'))
                else:
                    flash('El integrante 2 no se encuentra registrado en el sistema')
                    return redirect(url_for('estudiantes.registroproyecto_segunda'))
        elif n_integrantes == '3':
            integrante_uno = get_user(request.form['integrante_1'])
            integrante_dos = get_user(request.form['integrante_2'])
            integrante_tres = get_user(request.form['integrante_3'])
            if verificar_usuario(request.form['integrante_2']) and verificar_usuario(request.form['integrante_3']):
                integrante_dos = get_user(request.form['integrante_2'])
                integrante_tres = get_user(request.form['integrante_3'])
            else:
                if entrega == '1era Entrega':
                    flash('El integrante 2 o 3 no se encuentra registrado en el sistema')
                    return redirect(url_for('estudiantes.registroproyecto'))
                else:
                    flash('El integrante 2 o 3 no se encuentra registrado en el sistema')
                    return redirect(url_for('estudiantes.registroproyecto_segunda'))
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
        proyecto = Proyectos(nombrep, ciclo, integrante_dos, integrante_tres, integrante_uno, 11, fecha_hora, hash_trans_proyecto, hash_trans_anexos, entrega)
        proyecto.set_proyecto()
        # obtener el id del proyecto
        flash('Proyecto registrado correctamente')
        return redirect(url_for('estudiantes.perfilestudiante'))
    else:
        flash('Error al registrar el proyecto')
        return redirect(url_for('estudiantes.registroproyecto'))
def get_user(num_doc):
    sql_user = "SELECT * FROM projecto_usuario WHERE doc_identidad = '{0}'".format(num_doc)
    cursor.execute(sql_user)
    id_user = cursor.fetchone()
    if id_user is not None:
        return id_user[0]
    else:
        return None
def verificar_usuario(num_doc):
    sql_user = " SELECT * FROM projecto_usuario WHERE doc_identidad = '{0}'".format(num_doc)
    cursor.execute(sql_user)
    id_user = cursor.fetchone()
    if id_user is not None:
        return True
    else:
        return False
# def proyecto_enviar(nombrep, ciclo, integrante_uno, integrante_dos, integrante_tres, doc_proyecto, doc_anexos, entrega):
#     fs = ipfshttpclient.connect('/ip4/10.73.48.83/tcp/5001')
#     # Instancia de web3 para envio de transacción a blockchain
#     w3 = conection_eth()
#     up_projecto_file = fs.add(doc_proyecto)
#     hash_ipfs_projecto=up_projecto_file.get('Hash')
#     data_projecto=w3.toHex(text=hash_ipfs_projecto)
#     tx_projecto={
#         'from': "0xbB98661629e0d9263F527acB44084BFDB0d9b86c",
#         'value': 0,
#         'gas': 2000000,
#         'gasPrice': w3.toWei('1', 'gwei'),
#         'data': data_projecto
#     }
#     tx_send_trans_proyecto = w3.eth.sendTransaction(tx_projecto)
#     hash_trans_proyecto = tx_send_trans_proyecto.hex()
        
#     if doc_anexos.filename == '':
#         hash_trans_anexos = 'Sin anexos'
#     else:
#         # Se cambia el nombre del documento dependiendo del nombre del proyecto
#         doc_anexos.name = nombrep + "_anexos.pdf"
#             # Se guarda el documento en IPFS
#         up_anexos_file = fs.add(doc_anexos)
#             # Se guarda el hash en variables para parcealas a hexadecimal para subir a la blockchain
#         hash_ipfs_anexos=up_anexos_file.get('Hash')
#             # Se convierte el hash a hexadecimal
#         data_anexos=w3.toHex(text=hash_ipfs_anexos)
#         tx_anexos={
#             'from': "0xbB98661629e0d9263F527acB44084BFDB0d9b86c",
#             'value': 0,
#             'gas': 2000000,
#             'gasPrice': w3.toWei('1', 'gwei'),
#             'data': data_anexos
#         }
#             # se envia la transacciones 
#         tx_send_trans_anexos = w3.eth.sendTransaction(tx_anexos)
#             # Se obtiene el hash de la transacción para cada documento
#         hash_trans_anexos = tx_send_trans_anexos.hex()
        
#         fecha_hora = datetime.now() 
#         #Generar fecha y hora
        
#         # Se guarda el proyecto en la base de datos
#         proyecto = Proyectos(nombrep, ciclo, integrante_dos, integrante_tres, integrante_uno, 11, fecha_hora, hash_trans_proyecto, hash_trans_anexos, entrega)
#         proyecto.set_proyecto()

@estudiantes.route('/perfilestudiante')
@login_required
def perfilestudiante():
    flash('Bienvenido {0}'.format(current_user.nombres))
    w3 = conection_eth()
    sql_usuario = "SELECT * FROM projecto_usuario"
    cursor.execute(sql_usuario)
    usuarios = cursor.fetchall()
    sql_proyectos_all="SELECT * FROM projecto_proyecto"
    cursor.execute(sql_proyectos_all)
    proyectos_all=cursor.fetchall()
    proyectos_parceado=[]
    for proyecto in proyectos_all:
        if proyecto[5]=='Sin anexos':
            proyectos_parceado.append([proyecto[0], proyecto[1],proyecto[2],proyecto[3],w3.eth.getTransaction(proyecto[4]).input,'Sin anexos',proyecto[6],proyecto[7],proyecto[8],proyecto[9],proyecto[10],proyecto[11]])
        else:
            proyectos_parceado.append([proyecto[0], proyecto[1],proyecto[2],proyecto[3],w3.eth.getTransaction(proyecto[4]).input,w3.eth.getTransaction(proyecto[5]).input,proyecto[6],proyecto[7],proyecto[8],proyecto[9],proyecto[10],proyecto[11]])

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
    if fecha_hoy >= fecha_entrega_inicio_e2 and fecha_hoy < fecha_entrega_fin_e2:
        estado_entrega_e2 = True
    else:
        estado_entrega_e2 = False
    
    calif_obser=[]
    # Traer usuario 
    sql_usuario = "SELECT * FROM projecto_usuario WHERE id = '{0}'".format(current_user.id)
    cursor.execute(sql_usuario)
    usuario = cursor.fetchone()
    # Traer los proyectos donde el usuario esta inscrito
    sql_proyectos = "SELECT * FROM projecto_proyecto WHERE estudiante_uno_id = '{0}' OR estudiante_dos_id = '{0}' OR estudiante_tres_id = '{0}'".format(current_user.id)
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
                    observ_1=w3.eth.getTransaction(calif[8]).input
                    calif_obser.append([proyects[11],calif[0],calif[2], nota_1, observ_1])
            elif proyects[11] == 2:
                if calif[3] == None or calif[4] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    observ_1=w3.eth.getTransaction(calif[8]).input
                    observ_2=w3.eth.getTransaction(calif[9]).input
                    calif_obser.append([proyects[11],calif[0],calif[2], nota_1, nota_2, observ_1, observ_2])
            elif proyects[11] == 3:
                if calif[3] == None or calif[4] == None or calif[5] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    observ_1=w3.eth.getTransaction(calif[8]).input
                    observ_2=w3.eth.getTransaction(calif[9]).input
                    observ_3=w3.eth.getTransaction(calif[10]).input
                    calif_obser.append([proyects[11],calif[0],calif[2], nota_1, nota_2, nota_3, observ_1, observ_2, observ_3])
            elif proyects[11] == 4:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    observ_1=w3.eth.getTransaction(calif[8]).input
                    observ_2=w3.eth.getTransaction(calif[9]).input
                    observ_3=w3.eth.getTransaction(calif[10]).input
                    observ_4=w3.eth.getTransaction(calif[11]).input
                    calif_obser.append([proyects[11],calif[0],calif[2], nota_1, nota_2, nota_3, nota_4, observ_1, observ_2, observ_3, observ_4])
            elif proyects[11] == 5:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None or calif[7] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    nota_5=w3.eth.getTransaction(calif[7]).input
                    observ_1=w3.eth.getTransaction(calif[8]).input
                    observ_2=w3.eth.getTransaction(calif[9]).input
                    observ_3=w3.eth.getTransaction(calif[10]).input
                    observ_4=w3.eth.getTransaction(calif[11]).input
                    observ_5=w3.eth.getTransaction(calif[12]).input
                    calif_obser.append([proyects[11],calif[0],calif[2], nota_1, nota_2, nota_3, nota_4, nota_5, observ_1, observ_2, observ_3, observ_4, observ_5])
    
    return render_template("perfilEstudiante.html", usuarios=usuarios,fecha=fechas, cal_ob=calif_obser, estado_e1=estado_entrega_e1, estado_e2=estado_entrega_e2, allproyectos=proyectos_parceado)
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


