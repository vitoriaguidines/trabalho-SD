// Antes de rodar, verifique se o seu ambiente está preparado
// Inicializar o projeto (já foi feito): npm init -y
// Instalar as dependências: npm install express mysql
// Adicione as variáveis de ambiente

// Inicie o servidor: node app.js
// Equanto o servidor estiver no ar: http://localhost:3000/filmes

// Se aparecer o erro "ER_NOT_SUPPORTED_AUTH_MODE", tente: ALTER USER 'seu_usuario'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'sua_senha'; 

const express = require('express');
const mysql = require('mysql');

const app = express();
const port = 3000;

// Configurar a conexão com o banco de dados
const db = mysql.createConnection({
  host: 'localhost',
  user: 'usuario', // Usuário do MySql
  password: 'senha', // Senha do MySql
  database: 'sakila',
});

// Conectar ao banco de dados
db.connect((err) => {
  if (err) {
    console.error('Erro ao conectar ao banco de dados: ' + err.message);
  } else {
    console.log('Conectado ao banco de dados Sakila');
  }
});

// Rota para obter dados de exemplo
app.get('/filmes', (req, res) => {
  db.query('SELECT * FROM film LIMIT 10', (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      res.json(results);
    }
  });
});

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor web iniciado em http://localhost:${port}`);
});
