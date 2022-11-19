from flask import Blueprint, render_template, request, redirect, url_for, flash
formulario = Blueprint('formulario',__name__, url_prefix='/forms', template_folder='templates')
from config import *
from flask_login import login_user, logout_user, current_user
from .usuario import Usuarios, Usuario
from flask_mail import Mail, Message
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
                        flash('Contraseña incorrecta')
                        return redirect(url_for('formulario.login')) 
                #    Si el rol es uno dirigir a la vista de perfilestudiante
                else:
                    flash('Usuario no registrado')
                    return redirect(url_for('formulario.login'))
            except:
                flash('Usuario no registrado')
                return redirect(url_for('formulario.login'))
        else:
            flash('Por favor ingrese todos los campos')
            return redirect(url_for('formulario.login'))
    else:
        flash('Por favor ingrese todos los campos')
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
        # Verificar que el numeo de identificacion no este registrado
        sql="SELECT id FROM projecto_usuario WHERE doc_identidad='{0}'".format(numero_identificacion)
        cursor = con_bd.cursor()
        cursor.execute(sql)
        user_consult=cursor.fetchone()
        if user_consult is None:
            # Verificar que el correo no este registrado
            sql="SELECT id FROM projecto_usuario WHERE correo='{0}'".format(email_institucional)
            cursor = con_bd.cursor()
            cursor.execute(sql)
            user_consult=cursor.fetchone()
            if user_consult is None:
                # Registrar el usuario
                usuario = Usuarios(nombres, apellidos, email_institucional, numero_identificacion, contraseña, tipo_rol, tipo_documento)
                usuario.set_usuario()
                flash('Usuario registrado correctamente')
                return redirect(url_for('formulario.login'))
            else:
                flash('El correo ya se encuentra registrado')
                return redirect(url_for('formulario.registro'))
        else:
            flash('El numero de identificacion ya se encuentra registrado')
            return redirect(url_for('formulario.registro'))
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
        if nombres and apellidos and tipo_documento and tipo_rol and numero_identificacion and email_institucional and contraseña:
            # Verificar que el numero de identificacion
            # no se encuentre registrado
            sql="SELECT id FROM projecto_usuario WHERE numero_identificacion='{0}'".format(numero_identificacion)
            cursor = con_bd.cursor()
            cursor.execute(sql)
            user_consult=cursor.fetchone()
            if user_consult is None:
                # Verificar que el correo no se encuentre registrado
                sql="SELECT id FROM projecto_usuario WHERE correo='{0}'".format(email_institucional)
                cursor = con_bd.cursor()
                cursor.execute(sql)
                user_consult=cursor.fetchone()
                if user_consult is None:
                    # Registrar el usuario
                    usuario = Usuarios(nombres, apellidos, email_institucional, numero_identificacion, contraseña, tipo_rol, tipo_documento)
                    usuario.set_usuario()
                    flash('Usuario registrado correctamente')
                    return redirect(url_for('formulario.login'))
                else:
                    flash('El correo ya se encuentra registrado')
                    return redirect(url_for('formulario.registro'))
            else:
                flash('El numero de identificacion ya se encuentra registrado')
                return redirect(url_for('formulario.registro'))
        else:
            flash('Por favor ingrese todos los campos')
            return redirect(url_for('formulario.registro'))
    else:
        return redirect(url_for('formulario.registro'))
    #     usuario = Usuarios(nombres, apellidos, email_institucional, numero_identificacion, contraseña, tipo_rol, tipo_documento)
    #     usuario.set_usuario()
    #     return redirect(url_for('admin.perfiladmin'))
    # else:
    #     return redirect(url_for('formulario.registro'))

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

    



  




