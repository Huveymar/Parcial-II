from flask import render_template, request
from src import app

@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('inicio.html')

