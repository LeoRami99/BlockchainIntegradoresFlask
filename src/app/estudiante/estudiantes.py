from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from web3 import Web3
import ipfshttpclient
from .proyecto import Proyectos
from config import *
conn = EstablecerConexion()
cursor = conn.cursor()
estudiantes= Blueprint('estudiantes',__name__,url_prefix='/estudiantes', template_folder='templates')
@estudiantes.route('/registroproyecto')
def registroproyecto():
    return render_template("registroProyecto.html")

@estudiantes.route('/registrar_proyecto', methods=['POST'])
def registrar_proyecto():
    # Instancia de la conexión a IPFS
    fs = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    # Instancia de web3 para envio de transacción a blockchain
    w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
    
    # Variables para guardar los integrantes del equipo
    if request.method == 'POST':
        integrante_dos='1'
        integrante_tres='1'
        ciclo = request.form['ciclo']
        n_integrantes = request.form['numero_miembros']
        integrante_1 = request.form['integrante_1']
        if n_integrantes == '2':
            integrante_dos = request.form['integrante_dos']
            integrante_tres = '1'
        elif n_integrantes == '3':
            integrante_dos = request.form['integrante_dos']
            integrante_tres = request.form['integrante_tres']
        
        # integrante_2 = request.form['integrante_2']
        # integrante_3 = request.form['integrante_3']
        nombrep = request.form['nombrep']
        doc_proyecto = request.files['docfile']
        doc_anexos = request.files['anexos_proyecto']
        # Se cambia el nombre del documento dependiendo del nombre del proyecto
        doc_proyecto.name = nombrep + ".pdf"
        doc_anexos.name = nombrep + "_anexos.pdf"
        # Se guarda el documento en IPFS
        up_projecto_file = fs.add(doc_proyecto)
        up_anexos_file = fs.add(doc_anexos)
        # Se guarda el hash en variables para parcealas a hexadecimal para subir a la blockchain
        hash_ipfs_projecto=up_projecto_file.get('Hash')
        hash_ipfs_anexos=up_anexos_file.get('Hash')
        # Se convierte el hash a hexadecimal
        data_projecto=w3.toHex(text=hash_ipfs_projecto)
        data_anexos=w3.toHex(text=hash_ipfs_anexos)
        tx_projecto={
            'from': "0xbB98661629e0d9263F527acB44084BFDB0d9b86c",
            'value': 0,
            'gas': 2000000,
            'gasPrice': w3.toWei('1', 'gwei'),
            'data': data_projecto
        }
        tx_anexos={
            'from': "0xbB98661629e0d9263F527acB44084BFDB0d9b86c",
            'value': 0,
            'gas': 2000000,
            'gasPrice': w3.toWei('1', 'gwei'),
            'data': data_anexos
        }
         # se envia la transacciones 
        tx_send_trans_proyecto = w3.eth.sendTransaction(tx_projecto)
        tx_send_trans_anexos = w3.eth.sendTransaction(tx_anexos)
        # Se obtiene el hash de la transacción para cada documento
        hash_trans_proyecto = tx_send_trans_proyecto.hex()
        hash_trans_anexos = tx_send_trans_anexos.hex()
        #Generar fecha y hora
        fecha_hora = datetime.now() 
        get_user(integrante_1)
        # Se guarda el proyecto en la base de datos
        proyecto = Proyectos(nombrep, ciclo, int(get_user(integrante_1)), integrante_dos, integrante_tres, ciclo,fecha_hora,hash_trans_proyecto,hash_trans_anexos)
        proyecto.set_proyecto()
        return redirect(url_for('estudiantes.perfilestudiante'))
    else:
        return redirect(url_for('estudiantes.registroproyecto'))
def get_user(num_doc):
 
    sql = "SELECT * FROM projecto_usuario WHERE doc_identidad = '{0}'".format(num_doc)
    cursor.execute(sql)
    id_usuario=cursor.fetchone()
    print("Este es el id del usuario: ", id_usuario)
    return id_usuario[0]
        
        
        

        
    
@estudiantes.route('/perfilestudiante')
def perfilestudiante():
    return render_template("perfilEstudiante.html")
