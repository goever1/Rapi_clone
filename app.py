from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:0000@localhost/rappidb'
db = SQLAlchemy(app)

from models import TipoComida, Comida, Restaurante

# Ruta para obtener todos los tipos de comida
@app.route('/tiposcomida', methods=['GET'])
def get_tiposcomida():
    tiposcomida = TipoComida.query.all()
    tiposcomida_json = [{'id': tipo.TipoComidaID, 'nombre': tipo.NombreTipoComida} for tipo in tiposcomida]
    return jsonify({'tiposcomida': tiposcomida_json})

# Ruta para obtener todas las comidas de un tipo de comida específico
@app.route('/comidas/<int:tipo_comida_id>', methods=['GET'])
def get_comidas_por_tipo(tipo_comida_id):
    comidas = Comida.query.filter_by(TipoComidaID=tipo_comida_id).all()
    comidas_json = [{'id': comida.ComidaID, 'nombre': comida.NombreComida, 'precio': float(comida.Precio)} for comida in comidas]
    return jsonify({'comidas': comidas_json})

# Ruta para obtener todos los restaurante
@app.route('/restaurantes', methods=['GET'])
def get_restaurantes():
    restaurantes = Restaurante.query.all()
    restaurantes_json = [{'id': restaurante.RestauranteID, 'nombre': restaurante.NombreRestaurante, 'direccion': restaurante.Direccion} for restaurante in restaurantes]
    return jsonify({'restaurantes': restaurantes_json})

if __name__ == '__main__':
    app.run(debug=True)
