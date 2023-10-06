USE rappidb;
CREATE TABLE TipoComida (
    TipoComidaID INT AUTO_INCREMENT PRIMARY KEY,
    NombreTipoComida VARCHAR(255) NOT NULL
);
CREATE TABLE Restaurante (
    RestauranteID INT AUTO_INCREMENT PRIMARY KEY,
    NombreRestaurante VARCHAR(255) NOT NULL,
    Direccion VARCHAR(255) NOT NULL,
    Telefono VARCHAR(20)
);
CREATE TABLE Comida (
    ComidaID INT AUTO_INCREMENT PRIMARY KEY,
    NombreComida VARCHAR(255) NOT NULL,
    Descripcion TEXT,
    Precio DECIMAL(10, 2) NOT NULL,
    TipoComidaID INT,
    RestauranteID INT,
    FOREIGN KEY (TipoComidaID) REFERENCES TipoComida(TipoComidaID),
    FOREIGN KEY (RestauranteID) REFERENCES Restaurante(RestauranteID)
);