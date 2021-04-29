from flask import render_template, request, redirect, url_for
from src.models.materias import Materias
from src.models.sesiones import Sesiones
from src.models.estudiantes import Estudiantes
from src import app

@app.route('/sesiones', methods=['GET', 'POST'])
def sesiones():
    model_sesiones = Sesiones()
    modelo_materias = Materias()
    sesiones1 = model_sesiones.get_sesiones()
    sesiones = []

    for sesion in sesiones1:
        materia = modelo_materias.get_materia(sesion[1])[1]
        sesiones.append([sesion[0],materia,sesion[2],sesion[3],sesion[4]])

    if request.method == 'GET':
        return render_template('sesiones.html', sesiones=sesiones)

@app.route('/sesiones/nueva', methods=['GET', 'POST'])
def nuevaSesion():
    modelo_materias = Materias()
    materias = modelo_materias.get_materias()

    if request.method == 'GET':
        return render_template('nuevaSesion.html', materias=materias)
    
    materia = request.form.get('materia')
    fecha = request.form.get('fecha')
    hora_inicio = request.form.get('hora_inicio')
    hora_fin = request.form.get('hora_fin')

    datos = [materia,fecha,hora_inicio,hora_fin]
    model_sesiones = Sesiones()
    model_sesiones.guardar(datos)

    return redirect(url_for('sesiones'))

@app.route('/sesiones/editar/<id>', methods=['GET', 'POST'])
def editarSesion(id):
    model_sesiones = Sesiones()
    sesion = model_sesiones.get_sesion(id)
    modelo_materias = Materias()
    materias = modelo_materias.get_materias()

    if request.method == 'GET':
        return render_template('editarSesion.html', sesion=sesion, materias=materias)
    
    materia = request.form.get('materia')
    fecha = request.form.get('fecha')
    hora_inicio = request.form.get('hora_inicio')
    hora_fin = request.form.get('hora_fin')

    datos = [id,materia,fecha,hora_inicio,hora_fin]
    model_sesiones.editar(datos)

    return redirect(url_for('sesiones'))

@app.route('/sesiones/eliminar/<id>', methods=['GET', 'POST'])
def eliminarSesion(id):
    model_sesiones = Sesiones()
    model_sesiones.eliminar(id)

    return redirect(url_for('sesiones'))

@app.route('/sesiones/asistencia/<id>', methods=['GET', 'POST'])
def listarAsistencia(id):
    model_sesiones = Sesiones()
    modelo_materias = Materias()
    model_estudiantes = Estudiantes()

    estudiantes = model_estudiantes.get_estudiantes()
    sesion1 = model_sesiones.get_sesion(id)
    materia = modelo_materias.get_materia(sesion1[1])[1]

    sesion = [sesion1[0],materia,sesion1[2],sesion1[3],sesion1[4]]
    
    return render_template('asistencia.html', sesion=sesion, estudiantes=estudiantes)
    