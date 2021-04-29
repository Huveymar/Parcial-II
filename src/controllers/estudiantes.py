from flask import render_template, request, redirect, url_for
from src import app
from src.models.estudiantes import Estudiantes

@app.route('/estudiantes', methods=['GET', 'POST'])
def estudiantes():
    modelo_estudiantes = Estudiantes()

    if request.method == 'GET':
        return render_template('estudiantes.html', estudiantes=modelo_estudiantes.get_estudiantes())

@app.route('/estudiantes/nuevo', methods=['GET', 'POST'])
def nuevoEstudiante():
    if request.method == 'GET':
        return render_template('crearEstudiante.html')

    identificacion = request.form.get('identificacion')
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    celular = request.form.get('celular')
    email = request.form.get('email')
    semestre = request.form.get('semestre')
    
    datos = [identificacion, nombres, apellidos, celular, email, semestre]

    modelo_estudiantes = Estudiantes()
    modelo_estudiantes.guardar(datos)

    return redirect(url_for('estudiantes'))

@app.route('/estudiantes/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    modelo_estudiantes = Estudiantes()
    estudiante = modelo_estudiantes.get_estudiante(id)

    if request.method == 'GET':
        return render_template('editarEstudiante.html', estudiante=estudiante)
    
    identificacion = request.form.get('identificacion')
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    celular = request.form.get('celular')
    email = request.form.get('email')
    semestre = request.form.get('semestre')
    
    datos = [id, identificacion, nombres, apellidos, celular, email, semestre]
    modelo_estudiantes.editar(datos)

    return redirect(url_for('estudiantes'))

@app.route('/estudiantes/eliminar/<id>', methods=['GET', 'POST'])
def eliminar(id):
    modelo_estudiantes = Estudiantes()
    modelo_estudiantes.eliminar(id)

    return redirect(url_for('estudiantes'))