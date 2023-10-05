// app.js (Servicio de autenticación en Node.js y Express)
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

app.use(bodyParser.json());

// Modelo de usuario
const User = require('./models/User');

// Clave secreta para firmar el token JWT
const JWT_SECRET = 'clavesegura'; // Cambia esto por una clave segura en producción

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/templates/index.html');
});


app.get('/registro', (req, res) => {
    res.sendFile(__dirname + '/views/registro.html');
});
app.post('/register', async (req, res) => {
  try {
    const { email, password } = req.body;

    // Verifica si el usuario ya existe
    const existingUser = await User.findOne({ where: { email } });
    if (existingUser) {
      return res.status(409).json({ error: 'El usuario ya existe' });
    }

    // Hash de la contraseña
    const hashedPassword = await bcrypt.hash(password, 10);

    // Crea un nuevo usuario
    const newUser = await User.create({ email, password: hashedPassword });

    // En producción, podrías enviar una respuesta sin la contraseña hash
    return res.status(201).json({ message: 'Usuario registrado exitosamente' });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Error al registrar usuario' });
  }
});

app.get('/login', (req, res) => {
    res.sendFile(__dirname + '/templates/login.html');
});
app.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    // Busca al usuario por correo electrónico
    const user = await User.findOne({ where: { email } });

    if (!user) {
      return res.status(404).json({ error: 'Usuario no encontrado' });
    }

    // Compara la contraseña ingresada con la contraseña hash almacenada
    const validPassword = await bcrypt.compare(password, user.password);

    if (!validPassword) {
      return res.status(401).json({ error: 'Contraseña incorrecta' });
    }

    // Genera un token JWT
    const token = jwt.sign({ userId: user.id }, JWT_SECRET);

    // Envía el token como respuesta (en producción, puedes incluir más información en el token)
    return res.json({ token });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Error al iniciar sesión' });
  }
});

app.listen(3000, () => {
  console.log('Servicio de autenticación en funcionamiento en el puerto 3000');
});