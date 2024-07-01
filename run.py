from flask import Flask
from app.views import *

app = Flask(__name__)

app.route('/')(index)

#si te llega esta ruta, ejecutá este método
app.route('/api/getTurnos', methods=['GET'])(getTurnos)
app.route('/api/getTurnoById/<int:id>', methods=['GET'])(get_by_id)
app.route('/api/getTurnoByPatente/<string:patente_vehiculo>', methods=['GET'])(get_by_patente)
app.route('/api/crearTurno', methods=['POST'])(create_turno)
app.route('/api/modificarTurno/<int:id>', methods=['PUT'])(update_turno)
app.route('/api/modificarTurno/<string:patente>', methods=['PUT'])(update_turno)
app.route('/api/deleteTurno/<int:id>', methods=['DELETE'])(delete_turno)
app.route('/api/deleteTurno/<string:patente>', methods=['DELETE'])(delete_turno_by_patente)

if __name__ == '__main__':
    app.run(debug=True)