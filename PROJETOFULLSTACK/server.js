var http = require('http');
var express = require('express');
var app = express();
require('colors');

app.use(express.static("./public"));

var server = http.createServer(app);

server.listen(3000);
console.log("Servidor rodando...".rainbow);