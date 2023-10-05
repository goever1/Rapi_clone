// models/User.js
const { DataTypes } = require('sequelize');
const sequelize = require('../database'); // Reemplaza con la ubicación de tu configuración de la base de datos

const User = sequelize.define('User', {
  email: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  password: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

module.exports = User;