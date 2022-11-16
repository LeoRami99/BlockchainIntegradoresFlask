from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from config import *
from config_eth import *
from flask_login import login_required, current_user
from .calificacion import Calificacion
conn = EstablecerConexion()
cursor = conn.cursor()
w3 = conection_eth()
jurado= Blueprint('jurado',__name__,url_prefix='/jurado', template_folder='templates')
@jurado.route('/perfiljurado')
@login_required
def perfiljurado():
    sql="SELECT * FROM projecto_proyecto"
    cursor.execute(sql)
    proyecto = cursor.fetchall()
    sql_usuarios = "SELECT * FROM projecto_usuario"
    cursor.execute(sql_usuarios)
    usuarios = cursor.fetchall()
    sql_calificaciones = "SELECT * FROM projecto_calificaciones"
    cursor.execute(sql_calificaciones)
    calificaciones = cursor.fetchall()
    sql_juradosciclo = "SELECT * FROM projecto_juradosciclo"
    cursor.execute(sql_juradosciclo)
    juradosciclo = cursor.fetchall()
    proyecto2 = []
    jurado_cali_1=[]
    jurado_cali_2=[]
    jurado_cali_3=[]
    jurado_cali_4=[]
    jurado_cali_5=[]
    # for jurado,calif in zip(calificaciones,juradosciclo):
    for proyect in proyecto:
        sql_jurados="SELECT * FROM projecto_juradosciclo WHERE id_jurado_ciclo = {}".format(proyect[9])
        cursor.execute(sql_jurados)
        jurado = cursor.fetchone()
        for calif in calificaciones:
            if calif[2]==proyect[0]:
                jurado_cali_1.append([calif[2],calif[3],jurado[4]])
                jurado_cali_2.append([calif[2],calif[4],jurado[2]])
                jurado_cali_3.append([calif[2],calif[5],jurado[3]])
                jurado_cali_4.append([calif[2],calif[6],jurado[5]])
                jurado_cali_5.append([calif[2],calif[7],jurado[6]])  
    # Hacer la verificación por poryecto si ya el jurado correspondiente ya califico
    # Condición para la casilla de jurado 1
    for proyect in proyecto:
        for nota in jurado_cali_1:
            if proyect[0]==nota[0]:
                if nota[2]==current_user.id:
                    if nota[1]==None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                    elif nota[1]!=None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
    # Condición para la casilla de jurado 2
    for proyect in proyecto:
        for nota in jurado_cali_2:
            if proyect[0]==nota[0]:
                if nota[2]==current_user.id:
                    if nota[1]==None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                    elif nota[1]!=None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
    # Condición para la casilla de jurado 3
    for proyect in proyecto:
        for nota in jurado_cali_3:
            if proyect[0]==nota[0]:
                if nota[2]==current_user.id:
                    if nota[1]==None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                    elif nota[1]!=None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
    # Condición para la casilla de jurado 4
    for proyect in proyecto:
        for nota in jurado_cali_4:
            if proyect[0]==nota[0]:
                if nota[2]==current_user.id:
                    if nota[1]==None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                    elif nota[1]!=None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
    # Condición para la casilla de jurado 5
    for proyect in proyecto:
        for nota in jurado_cali_5:
            if proyect[0]==nota[0]:
                if nota[2]==current_user.id:
                    if nota[1]==None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], False])
                    elif nota[1]!=None:
                        if proyect[5]=="Sin anexos":
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, 'Sin anexos', get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
                        else:
                            proyecto2.append([proyect[0], proyect[1], proyect[2], w3.eth.getTransaction(proyect[4]).input, w3.eth.getTransaction(proyect[5]).input, get_usuario_nombre(proyect[8]), get_usuario_nombre(proyect[6]), get_usuario_nombre(proyect[7]), proyect[10], True])
                       
    return render_template('perfilJurado.html',proyecto=proyecto2, proyectos=proyecto)
        
        
        
    
            
            


                
        
    # para poder mostrarlos en la vista
    # for i in proyecto:
    #     if i[5]=='Sin anexos':
    #         proyecto2.append([i[0],i[1],i[2],i[3],w3.eth.getTransaction(i[4]).input,'Sin anexos',get_usuario_nombre(i[6]),get_usuario_nombre(i[7]),get_usuario_nombre(i[8]),i[9],i[10], i[11]])
    #     else:
    #         proyecto2.append([i[0],i[1],i[2],i[3],w3.eth.getTransaction(i[4]).input,w3.eth.getTransaction(i[5]).input,get_usuario_nombre(i[6]),get_usuario_nombre(i[7]),get_usuario_nombre(i[8]),i[9],i[10], i[11]])
    return render_template('perfilJurado.html', proyectos=proyecto2, usuario=usuarios, calificaciones=calificaciones, juradosxciclo=juradosciclo)
def get_usuario_nombre(id_user):
    id_usuario=str(id_user)
    sql_usuari = "SELECT * FROM projecto_usuario WHERE id = %s"
    cursor.execute(sql_usuari, (id_usuario))
    usuario = cursor.fetchone()
    return usuario[1]

@jurado.route('/retroalimentacion', methods=['POST'])
def retroalimentacion():
    if request.method == 'POST':
        id_proyecto = request.form['id_proyecto']
        calificacion = request.form['calificacion']
        id_jurado = request.form['id_jurado']
        observaciones = request.form['observaciones']
        ciclo = request.form['ciclo']
        entrega = request.form['entrega']
        if entrega == '2da entrega':
            item_1=request.form['item-1']
            item_2=request.form['item-2']
            item_3=request.form['item-3']
            item_4=request.form['item-4']
            item_5=request.form['item-5']
            item_6=request.form['item-6']
            item_7=request.form['item-7']
            item_8=request.form['item-8']
            item_9=request.form['item-9']
            item_10=request.form['item-10']
            calificacion = request.form['calificacion']
            promedio=(float(item_1)+float(item_2)+float(item_3)+float(item_4)+float(item_5)+float(item_6)+float(item_7)+float(item_8)+float(item_9)+float(item_10)+ float(calificacion))/11
        else:
            promedio = calificacion

        data_calificacion=w3.toHex(text=promedio)
        
        data_observaciones=w3.toHex(text=observaciones)
        tx_calificacion={
            'from': "0xbB98661629e0d9263F527acB44084BFDB0d9b86c",
            'value': 0,
            'gas': 2000000,
            'gasPrice': w3.toWei('1', 'gwei'),
            'data': data_calificacion
        }
        tx_observaciones={
            'from': "0xbB98661629e0d9263F527acB44084BFDB0d9b86c",
            'value': 0,
            'gas': 2000000,
            'gasPrice': w3.toWei('1', 'gwei'),
            'data': data_observaciones
        }
         # se envia la transacciones 
        tx_send_trans_califacion = w3.eth.sendTransaction(tx_calificacion)
        tx_send_trans_observacion = w3.eth.sendTransaction(tx_observaciones)
        # Se obtiene el hash de la transacción para cada documento
        hash_trans_califacion = tx_send_trans_califacion.hex()
        hash_trans_observacion = tx_send_trans_observacion.hex()
        sql_proyecto="SELECT jurados_ciclo_id FROM projecto_proyecto WHERE id_proyecto = {}".format(int(id_proyecto))
        cursor.execute(sql_proyecto)
        jurados_ciclo_id = cursor.fetchone()
        sql_grupo_jurado="SELECT * FROM projecto_juradosciclo WHERE ciclo =%s and id_jurado_ciclo = %s"
        cursor.execute(sql_grupo_jurado, (ciclo, jurados_ciclo_id))
        grupo_jurado = cursor.fetchall()
        for jurado_casilla in grupo_jurado:
            if jurado_casilla[4]==int(id_jurado):
                calif_jurado_uno=Calificacion(id_proyecto,id_jurado,hash_trans_califacion, None, None, None, None, hash_trans_observacion, None, None, None, None)
                calif_jurado_uno.set_calificacion_observacion_jurado_uno()
                
            elif jurado_casilla[2]==int(id_jurado):
                calif_jurado_dos=Calificacion(id_proyecto,id_jurado,None,hash_trans_califacion, None, None, None, None, hash_trans_observacion, None, None, None)
                calif_jurado_dos.set_calificacion_observacion_jurado_dos()
                
            elif jurado_casilla[3]==int(id_jurado):
                calif_jurado_tres=Calificacion(id_proyecto,id_jurado,None,None, hash_trans_califacion, None, None, None, None, hash_trans_observacion, None, None)
                calif_jurado_tres.set_calificacion_observacion_jurado_tres()
                
            elif jurado_casilla[5]==int(id_jurado):
                calif_jurado_cuatro=Calificacion(id_proyecto,id_jurado,None,None, None,hash_trans_califacion,None, None, None, None, hash_trans_observacion, None)
                calif_jurado_cuatro.set_calificacion_observacion_jurado_cuatro()
                
            elif jurado_casilla[6]==int(id_jurado):

                calif_jurado_cinco=Calificacion(id_proyecto,id_jurado,None,None, None,None,hash_trans_califacion, None, None, None, None, hash_trans_observacion)
                calif_jurado_cinco.set_calificacion_observacion_jurado_cinco()
        return redirect(url_for('jurado.perfiljurado'))

    

        



