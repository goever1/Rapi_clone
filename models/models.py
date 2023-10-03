from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TipoComida(db.Model):
    __tablename__ = 'TipoComida'

    TipoComidaID = db.Column(db.Integer, primary_key=True)
    NombreTipoComida = db.Column(db.String(255), nullable=False)

class Comida(db.Model):
    __tablename__ = 'Comida'

    ComidaID = db.Column(db.Integer, primary_key=True)
    NombreComida = db.Column(db.String(255), nullable=False)
    Descripcion = db.Column(db.Text)
    Precio = db.Column(db.DECIMAL(10, 2), nullable=False)
    TipoComidaID = db.Column(db.Integer, db.ForeignKey('TipoComida.TipoComidaID'), nullable=False)
    RestauranteID = db.Column(db.Integer, db.ForeignKey('Restaurante.RestauranteID'), nullable=False)

    tipo_comida = db.relationship('TipoComida', backref='comidas')
    restaurante = db.relationship('Restaurante', backref='comidas')

class Restaurante(db.Model):
    __tablename__ = 'Restaurante'

    RestauranteID = db.Column(db.Integer, primary_key=True)
    NombreRestaurante = db.Column(db.String(255), nullable=False)
    Direccion = db.Column(db.String(255), nullable=False)
    Telefono = db.Column(db.String(20))

    comidas = db.relationship('Comida', backref='restaurante')
