from flask import Blueprint, render_template, request, redirect, url_for
formulario = Blueprint('formulario',__name__, url_prefix='/forms', template_folder='templates')
from config import *
from .usuario import Usuarios
con_bd = EstablecerConexion()
@formulario.route('/registro')
def registro():
    return render_template('registro.html')
@formulario.route('/login')
def login():
    return render_template('login.html')

@formulario.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        tipo_documento = request.form['tipo_documento']
        tipo_rol = request.form['tipo_rol']
        numero_identificacion = request.form['numero_identificacion']
        numero_universidad = request.form['numero_universidad']
        email_institucional = request.form['correoinstitucional']
        contraseña = request.form['contraseña']
        usuario = Usuarios(nombres, apellidos, email_institucional, numero_identificacion, numero_universidad, contraseña, 1, tipo_rol, tipo_documento)
        usuario.set_usuario()
        return redirect(url_for('formulario.login'))
    else:
        return redirect(url_for('formulario.registro'))


  




