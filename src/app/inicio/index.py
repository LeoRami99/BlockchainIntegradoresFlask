from flask import Blueprint, render_template, request, redirect, url_for
from config import *
# Creamos el Blueprint
inicio = Blueprint('inicio',__name__,url_prefix='/', template_folder='templates')
con_bd = EstablecerConexion()
@inicio.route('/')
def index():
    return redirect(url_for('formulario.login'))
    
