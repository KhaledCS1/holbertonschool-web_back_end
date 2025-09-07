const express = require('express');
const routes = require('./routes');

const app = express();
const port = 1245;

app.use('/', routes);

if (process.env.NODE_ENV !== 'test') {
	app.listen(port);
}

module.exports = app;
