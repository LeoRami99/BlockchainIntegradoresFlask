from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
formulario = Blueprint('formulario',__name__, url_prefix='/forms', template_folder='templates')
from config import *
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, current_user
import pickle
import base64
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
        if email_institucional.endswith("@ucundinamarca.edu.co"):
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
            flash('El correo no pertenece a la universidad')
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
        # solo acpetar correos institucionales
        contraseña = request.form['contraseña']
        if email_institucional.endswith("@ucundinamarca.edu.co"):
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
            flash('Por favor ingrese un correo institucional')
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
@formulario.route('/new_password/<token>', methods=['GET', 'POST'])
def forgot_password(token):
    if token is None:
        flash('Lo sentimos no puedes acceder a esta pagina')
        return redirect(url_for('formulario.login'))
    else:
        # verificar el token en la base de datos
        sql="SELECT id FROM projecto_usuario WHERE token_password='{0}'".format(token)
        cursor = con_bd.cursor()
        cursor.execute(sql)
        user_consult=cursor.fetchone()
        if user_consult is None:
            flash('Lo sentimos no puedes acceder a esta pagina')
            return redirect(url_for('formulario.login'))
        else:
            return render_template('forgot.html', token=token)
@formulario.route('/actualizar_password', methods=['GET', 'POST'])
def actualizar_password():
    if request.method == 'POST':
        contraseña = request.form['contrasena_uno']
        confirmar_contraseña = request.form['contrasena_dos']
        token = request.form['token']
        if contraseña and confirmar_contraseña and token:
            if contraseña == confirmar_contraseña:
                # Actualizar la contraseña
                sql="UPDATE projecto_usuario SET contrasena='{0}' WHERE token_password='{1}'".format(generate_password_hash(contraseña), token)
                cursor = con_bd.cursor()
                cursor.execute(sql)
                con_bd.commit()
                flash('Contraseña actualizada correctamente')
                return redirect(url_for('formulario.login'))
            else:
                flash('Las contraseñas no coinciden')
                return redirect(url_for('formulario.forgot_password', token=token))
        else:
            flash('Por favor ingrese todos los campos')
            return redirect(url_for('formulario.forgot_password', token=token))
    else:
        return redirect(url_for('formulario.login'))
@formulario.route('/reset_password', methods=['POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            # Verificar que el correo se encuentre registrado
            sql="SELECT id FROM projecto_usuario WHERE correo='{0}'".format(email)
            cursor = con_bd.cursor()
            cursor.execute(sql)
            user_consult=cursor.fetchone()
            if user_consult is None:
                flash('El correo no se encuentra registrado')
                return redirect(url_for('formulario.login'))
            else:
            #   generar un token para el usuario
                token = generate_token(email)
                msg = Message('Reseteo de contraseña', sender='juanlov4321@hotmail.com', recipients=[email])
                link = 'https://f8d6-186-84-89-9.ngrok.io/forms/new_password/' + token
                msg.html = render_template('correo.html', link=link)
                sql_token = "UPDATE projecto_usuario SET token_password='{0}' WHERE correo='{1}'".format(token, email)
                cursor = con_bd.cursor()
                cursor.execute(sql_token)
                con_bd.commit()
                with current_app.open_resource("static/imgs/FomalHauticon.png") as fp:
                    msg.attach("FomalHauticon.png", "image/png", fp.read(), 'inline', headers=[('Content-ID', '<image1>')])
                mail=Mail(current_app)
                mail.send(msg)
                flash('Se ha enviado un correo para recuperar la contraseña')
                return redirect(url_for('formulario.login'))
def generate_token(email):
    # generar un token aleatorio
    s = pickle.dumps(email)
    return base64.b64encode(s).decode("utf-8")

    



  




