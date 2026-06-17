var http = require("http");
var express = require("express");
var app = express();
var colors = require("colors");
const mongoose = require("mongoose");
mongoose.connect(
    "mongodb+srv://diegonc2007_db_user:W2OV9dg04l1nxxzx@cluster0.hgzlofw.mongodb.net/?appName=Cluster0"
)
.then(() => {
    console.log("Banco conectado");
})
.catch((erro) => {
    console.log(erro);
});


const PessoaSchema = new mongoose.Schema({
    nome:String,
    numero:Number
});
const Pessoa = mongoose.model(
    "Pessoa",
    PessoaSchema
);

app.use(express.static("./public"));
var server = http.createServer(app);
server.listen(3000);
console.log("Servidor funcionando...".rainbow);

app.set("view engine", "ejs");
app.set("views", "./views");
let bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());


app.get('/', async function(req,res){
    const pessoas = await Pessoa.find();
    var total = pessoas.length
    res.render("home", {pessoas:pessoas, total:total});
});

app.post('/salvar', async function(req,res){
    var nome = req.body.nomep;
    var numero = req.body.numerop;
    await Pessoa.create({
        nome:nome,
        numero:numero
    });
    const pessoas = await Pessoa.find();
    res.render("resposta", {nome,numero});
});