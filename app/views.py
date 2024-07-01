from flask import Flask, jsonify, request
from app.models import Turno
from app.database import get_db  
from datetime import datetime

def index():
    return '<h1>Lavadero Full Wash</h1>'

#GET
def getTurnos():
    # Llamo al modelo para que ejecute la funcion
    turnos = Turno.getTurnos()
    lista_turnos = [turno.serialize() for turno in turnos]
    return jsonify(lista_turnos)

def get_by_id(id):
    turno=Turno.get_by_id(id)
    if not turno: 
        return jsonify({'message': 'Turno no encontrado'}), 404
    return jsonify(turno.serialize())

def get_by_patente(patente_vehiculo):
    turno=Turno.get_by_patente(patente_vehiculo)
    if not turno: 
        return jsonify({'message': 'Patente no encontrada'}), 404
    return jsonify(turno.serialize())

#POST
def create_turno():
    data = request.get_json()    # Recepciono los datos enviados en la peticion en formato JSON
    nuevo_turno = Turno(
        # Extraigo datos del cuerpo de la solicitud
        fecha = data.get('fecha'),
        hora = data.get('hora'),
        nombre_persona = data['nombre_persona'],
        telefono_persona = data['telefono_persona'],
        mail_persona = data['mail_persona'],
        patente_vehiculo = data['patente_vehiculo'],
        servicio_descripcion = data['servicio_descripcion'],
        servicio_costo=data['servicio_costo']
    )
    nuevo_turno.guardar()
    return jsonify({'message':'Turno creado con exito'}), 201

#PUT
def update_turno(patente):
    turno = Turno.get_by_patente(patente)
    if not turno:
        return jsonify({'message': 'Turno no encontrado'}), 404
    #data = request.json
    data = request.get_json()
    # Extraigo datos del cuerpo de la solicitud
    turno.fecha = data.get('fecha')
    turno.hora = data.get('hora')
    turno.nombre_persona = data['nombre_persona']
    turno.telefono_persona = data['telefono_persona']
    turno.mail_persona = data['mail_persona']
    turno.patente_vehiculo = data['patente_vehiculo']
    turno.servicio_descripcion = data['servicio_descripcion']
    turno.servicio_costo=data['servicio_costo']
    
    turno.guardar()
    return jsonify({'message': 'Turno actualizado correctamente'}), 200

#DELETE
def delete_turno(id):
    turno = Turno.get_by_id(id)
    if not turno:
        return jsonify({'message': 'No existen registros para eliminar'}), 404
    turno.delete_by_id(id)
    return jsonify({'message': f'El registro {turno.id} fue eliminado con éxito'})

def delete_turno_by_patente(patente):
    turno = Turno.get_by_patente(patente)
    if not turno:
        return jsonify({'message': 'No existen registros para eliminar'}), 404
    turno.delete_by_patente(patente)
    return jsonify({'message': f'El registro {patente} fue eliminado con éxito'})