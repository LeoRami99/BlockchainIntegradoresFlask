from flask import Blueprint, render_template, request, redirect, url_for

admin= Blueprint('admin',__name__,url_prefix='/admin', template_folder='templates')
@admin.route('/perfiladmin')
def perfiladmin():
    return render_template("perfilAdministrador.html")