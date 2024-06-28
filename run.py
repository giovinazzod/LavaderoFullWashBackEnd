from flask import Flask
from app.views import *

app = Flask(__name__)

app.route('/')(index)

#si te llega esta ruta, ejecutá este método
app.route('/api/getAllTurnos', methods=['GET'])(getTurnos)
app.route('/api/get/<int:id>', methods=['GET'])(get_by_id)
app.route('/api/post', methods=['POST'])(post_turno)
app.route('/api/put', methods=['PUT'])(put_turno)
app.route('/api/delete', methods=['DELETE'])(delete_turno)

if __name__ == '__main__':
    app.run(debug=True)