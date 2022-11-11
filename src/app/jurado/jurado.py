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
    
    # para poder mostrarlos en la vista
    proyecto2 = []
    for i in proyecto:
        proyecto2.append([i[0],i[1],i[2],i[3],w3.eth.getTransaction(i[4]).input,w3.eth.getTransaction(i[5]).input,get_usuario_nombre(i[6]),get_usuario_nombre(i[7]),get_usuario_nombre(i[8]),i[9],i[10]])
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
        data_calificacion=w3.toHex(text=calificacion)
        
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
            print(jurado_casilla)
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

    

        



