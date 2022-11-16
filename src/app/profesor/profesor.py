from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from config import *
from config_eth import *
# from web3 import Web3

conn = EstablecerConexion()
cursor = conn.cursor()
w3 = conection_eth()
profesor= Blueprint('profesor',__name__,url_prefix='/profesor', template_folder='templates')
@profesor.route('/perfilprofesor')
@login_required
def perfilprofesor():
    sql="SELECT * FROM projecto_proyecto"
    cursor.execute(sql)
    proyecto = cursor.fetchall()
    sql_usuarios = "SELECT * FROM projecto_usuario"
    cursor.execute(sql_usuarios)
    usuarios = cursor.fetchall()
    sql_calificaciones = "SELECT * FROM projecto_calificaciones"
    cursor.execute(sql_calificaciones)
    calificaciones = cursor.fetchall()
    calif_obser=[]
    # # De proyecto los campos 4 y 5 son datos de la transacción se crea una nueva lista con esos datos
    # # para poder mostrarlos en la vista
    # proyecto2 = []
    # for i, cal_list in zip(proyecto, calificaciones):
    #     # traer el hash_del de la nota dependiendo el id del proyecto
    #     if cal_list[4] == i[0]:
    #         proyecto2.append([i[0],i[1],i[2],i[3],w3.eth.getTransaction(i[4]).input,w3.eth.getTransaction(i[5]).input,get_usuario_doc(i[6]),get_usuario_doc(i[7]),get_usuario_doc(i[8]),i[9],w3.eth.getTransaction(cal_list[1]).input, get_usuario_nombre(i[6]), get_usuario_nombre(i[7]), get_usuario_nombre(i[8])])
    # return render_template('perfilProfesor.html', proyectos=proyecto2, usuario=usuarios)
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
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_1])
            elif proyects[11] == 2:
                if calif[3] == None or calif[4] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_1, nota_2])
            elif proyects[11] == 3:
                if calif[3] == None or calif[4] == None or calif[5] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_1, nota_2, nota_3])
            elif proyects[11] == 4:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_1, nota_2, nota_3, nota_4])
            elif proyects[11] == 5:
                if calif[3] == None or calif[4] == None or calif[5] == None or calif[6] == None or calif[7] == None:
                    print('No hay calificacion')
                else:
                    nota_1=w3.eth.getTransaction(calif[3]).input
                    nota_2=w3.eth.getTransaction(calif[4]).input
                    nota_3=w3.eth.getTransaction(calif[5]).input
                    nota_4=w3.eth.getTransaction(calif[6]).input
                    nota_5=w3.eth.getTransaction(calif[7]).input
                    calif_obser.append([proyects[11],proyects[0],proyects[1],proyects[2],get_usuario_doc(proyects[8]),get_usuario_doc(proyects[6]),get_usuario_doc(proyects[7]),calif[0],calif[2], nota_1, nota_2, nota_3, nota_4, nota_5])
    return render_template('perfilProfesor.html', calif=calif_obser)

def get_usuario_doc(id_user):
    id_usuario=str(id_user)
    sql_usuari = "SELECT * FROM projecto_usuario WHERE id = %s"
    cursor.execute(sql_usuari, (id_usuario))
    usuario = cursor.fetchone()
    return usuario[4]
def get_usuario_nombre(id_user):
    id_usuario=str(id_user)
    sql_usuari = "SELECT nombre, apellidos FROM projecto_usuario WHERE id = %s"
    cursor.execute(sql_usuari, (id_usuario))
    usuario = cursor.fetchone()
    nombre_y_apellido = usuario[0] + " " + usuario[1]
    return nombre_y_apellido
