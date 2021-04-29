from flask import render_template, request, redirect, url_for
from src.models.materias import Materias
from src import app

@app.route('/materias', methods=['GET', 'POST'])
def materias():
    modelo_materias = Materias()
    materias = modelo_materias.get_materias()

    if request.method == 'GET':
        return render_template('materias.html', materias=materias)

@app.route('/materias/nueva', methods=['GET', 'POST'])
def nuevaMateria():
    if request.method == 'GET':
        return render_template('nuevaMateria.html')
    
    modelo_materias = Materias()
    nombre = request.form.get('nombre')
    semestre = request.form.get('semestre')

    datos = [nombre,semestre]
    modelo_materias.guardar(datos)

    return redirect(url_for('materias'))

@app.route('/materias/editar/<id>', methods=['GET', 'POST'])
def editarMateria(id):
    modelo_materias = Materias()
    materia = modelo_materias.get_materia(id)

    if request.method == 'GET':
        return render_template('editarMateria.html', materia=materia)
    
    nombre = request.form.get('nombre')
    semestre = request.form.get('semestre')

    datos = [id,nombre,semestre]
    modelo_materias.editar(datos)

    return redirect(url_for('materias'))

@app.route('/materias/eliminar/<id>', methods=['GET', 'POST'])
def eliminarMateria(id):
    modelo_materias = Materias()
    modelo_materias.eliminar(id)

    return redirect(url_for('materias'))