const express = require('express');
const app = express();

// Middleware
app.use(express.json());

// Route de base
app.get('/', (req, res) => {
    res.send('Bienvenue sur mon application Node.js !');
});

// Lancement du serveur
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Serveur démarré sur le port ${PORT}`);
});
