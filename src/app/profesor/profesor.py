from flask import Blueprint, render_template, request, redirect, url_for
from config import *
from web3 import Web3

conn = EstablecerConexion()
cursor = conn.cursor()
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
profesor= Blueprint('profesor',__name__,url_prefix='/profesor', template_folder='templates')
@profesor.route('/perfilprofesor')
def perfilprofesor():
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
        proyecto2.append([i[0],i[1],i[2],i[3],w3.eth.getTransaction(i[4]).input,w3.eth.getTransaction(i[5]).input,get_usuario_nombre(i[6]),get_usuario_nombre(i[7]),get_usuario_nombre(i[8]),i[9]])
    return render_template('perfilProfesor.html', proyectos=proyecto2, usuario=usuarios)

def get_usuario_nombre(id_user):
    id_usuario=str(id_user)
    sql_usuari = "SELECT * FROM projecto_usuario WHERE id = %s"
    cursor.execute(sql_usuari, (id_usuario))
    usuario = cursor.fetchone()
    return usuario[1]

