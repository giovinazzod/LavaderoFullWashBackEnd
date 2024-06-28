from flask import jsonify
from app.models import Turno
def index():
    return '<h1>Lavadero Full Wash</h1>'

def getTurnos():
    #acá llamo al modelo para que ejecute la funcion
    turnos = Turno.getTurnos()

    return jsonify(turnos)

def get_by_id(id):
    turno=Turno.get_by_id(id)
    if not turno: 
        return jsonify({'message': 'Turno not found'}), 404
    return jsonify(turno.serialize())

def post_turno():
    return '<h2>POST Turno</h2>'


def put_turno():
    return '<h2>PUT Turno</h2>'


def delete_turno():
    return '<h2>DELETE Turno</h2>'