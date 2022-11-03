from flask import Flask
# Instancias de los Blueprint
from app.formularios.form import formulario
from app.inicio.index import inicio
from app.estudiante.estudiantes import estudiantes
from app.profesor.profesor import profesor
from app.administrador.admin import admin
from app.jurado.jurado import jurado

# from app.correos.correo import correos


def createApp():
    app=Flask(__name__)
    # Registro de los Blueprint
    app.register_blueprint(inicio)
    app.register_blueprint(formulario)
    app.register_blueprint(estudiantes)
    app.register_blueprint(profesor)
    app.register_blueprint(admin)
    app.register_blueprint(jurado)

    return app