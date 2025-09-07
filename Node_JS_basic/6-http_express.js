const express = require('express');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

if (process.env.NODE_ENV !== 'test') {
  app.listen(port);
}

module.exports = app;