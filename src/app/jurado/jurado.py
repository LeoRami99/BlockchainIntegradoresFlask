from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from config import *
from web3 import Web3
from flask_login import login_required, current_user
from .calificacion import Calificacion
conn = EstablecerConexion()
cursor = conn.cursor()
w3 = Web3(Web3.HTTPProvider("http://192.168.0.13:8545"))
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

    # De proyecto los campos 4 y 5 son datos de la transacción se crea una nueva lista con esos datos
    # para poder mostrarlos en la vista
    proyecto2 = []
    for i in proyecto:
        proyecto2.append([i[0],i[1],i[2],i[3],w3.eth.getTransaction(i[4]).input,w3.eth.getTransaction(i[5]).input,get_usuario_nombre(i[6]),get_usuario_nombre(i[7]),get_usuario_nombre(i[8]),i[9],i[10]])
    return render_template('perfilJurado.html', proyectos=proyecto2, usuario=usuarios)
def get_usuario_nombre(id_user):
    id_usuario=str(id_user)
    sql_usuari = "SELECT * FROM projecto_usuario WHERE id = %s"
    cursor.execute(sql_usuari, (id_usuario))
    usuario = cursor.fetchone()
    return usuario[1]

@jurado.route('/retroalimentacion', methods=['POST'])
def retroalimentacion():
    if request.method == 'POST':
        calificacion = request.form['calificacion']
        observaciones = request.form['observaciones']
        fecha_hora = datetime.now() 
        id_proyecto = request.form['id_proyecto']
        id_jurado = request.form['id_usuario_jurado']
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
        calificacion = Calificacion(hash_trans_califacion, hash_trans_observacion, fecha_hora, id_proyecto, id_jurado)
        calificacion.set_calificaciones()
        return redirect(url_for('jurado.perfiljurado'))


