from flask import Blueprint, render_template, request, redirect, url_for
formulario = Blueprint('formulario',__name__, url_prefix='/forms', template_folder='templates')
from config import *
from flask_login import login_user, logout_user, current_user
from .usuario import Usuarios, Usuario
con_bd = EstablecerConexion()

# Establecer la secret key 
@formulario.route('/registro')
def registro():
    if current_user.is_authenticated:
        if current_user.rol == 1:
            return redirect(url_for('estudiantes.perfilestudiante'))
        elif current_user.rol == 2:
            return redirect(url_for('profesor.perfilprofesor'))
        elif current_user.rol == 3:
            return redirect(url_for('admin.perfiladmin'))
        elif current_user.rol == 4:
            return redirect(url_for('jurado.perfiljurado'))
    else:
        return render_template('registro.html')
@formulario.route('/login')
def login():
    if current_user.is_authenticated:
        if current_user.rol == 1:
            return redirect(url_for('estudiantes.perfilestudiante'))
        elif current_user.rol == 2:
            return redirect(url_for('profesor.perfilprofesor'))
        elif current_user.rol == 3:
            return redirect(url_for('admin.perfiladmin'))
        elif current_user.rol == 4:
            return redirect(url_for('jurado.perfiljurado'))
    else:
        return render_template('login.html')
@formulario.route('/logueo', methods=['POST'])
def logueo():
    if request.method == 'POST':
        correo = request.form['email_institucional']
        password = request.form['contrasena']
        if correo and password:
            try:
                sql="SELECT id FROM projecto_usuario WHERE correo='{0}'".format(correo)
                cursor = con_bd.cursor()
                cursor.execute(sql)
                user_consult=cursor.fetchone()

                user = Usuario(user_consult[0], correo, password)
                usuario_login = user.login(con_bd)
                if usuario_login != None:
                    if usuario_login.contrasena is True:
                        login_user(usuario_login)
                        if usuario_login.rol == 1:
                            return redirect(url_for('estudiantes.perfilestudiante'))
                        # Si el rol es dos dirigir a la vista de perfilprofesor
                        elif usuario_login.rol == 2:
                            return redirect(url_for('profesor.perfilprofesor'))
                        # Si el rol es tres dirigir a la vista de perfiladministrador
                        elif usuario_login.rol == 3:
                            return redirect(url_for('admin.perfiladmin'))
                        elif usuario_login.rol == 4:
                            return redirect(url_for('jurado.perfiljurado'))
                    else:
                        return redirect(url_for('formulario.login')) 
                #    Si el rol es uno dirigir a la vista de perfilestudiante
                else:
                    return redirect(url_for('formulario.login'))
            except:
                return redirect(url_for('formulario.login'))
        else:
            return redirect(url_for('formulario.login'))
    else:
        return redirect(url_for('formulario.login'))
@formulario.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('formulario.login'))
@formulario.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        tipo_documento = request.form['tipo_documento']
        tipo_rol = request.form['tipo_rol']
        numero_identificacion = request.form['numero_identificacion']
        email_institucional = request.form['correoinstitucional']
        contraseña = request.form['contraseña']
        usuario = Usuarios(nombres, apellidos, email_institucional, numero_identificacion, contraseña, tipo_rol, tipo_documento)
        usuario.set_usuario()
        return redirect(url_for('formulario.login'))
    else:
        return redirect(url_for('formulario.registro'))
@formulario.route('/registrar_docente', methods=['POST'])
def registrar_docente():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        tipo_documento = request.form['tipo_documento']
        tipo_rol = request.form['tipo_rol']
        numero_identificacion = request.form['numero_identificacion']
        email_institucional = request.form['correoinstitucional']
        contraseña = request.form['contraseña']
        usuario = Usuarios(nombres, apellidos, email_institucional, numero_identificacion, contraseña, tipo_rol, tipo_documento)
        usuario.set_usuario()
        return redirect(url_for('admin.perfiladmin'))
    else:
            return redirect(url_for('formulario.registro'))

@formulario.route('/registro_profesor')
def registro_profe():
    if current_user.is_authenticated:
        if current_user.rol == 1:
            return redirect(url_for('estudiantes.perfilestudiante'))
        elif current_user.rol == 2:
            return redirect(url_for('profesor.perfilprofesor'))
        elif current_user.rol == 3:
            return render_template('registroAdmin.html')
        elif current_user.rol == 4:
            return redirect(url_for('jurado.perfiljurado'))
    else:
        return redirect(url_for('formulario.login'))



  




