from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Inicial'

@app.route('/sobre')
def about():
    return 'Sobre'

@app.route('/colaboradores')
def peoples():
    return 'Colaboradores'