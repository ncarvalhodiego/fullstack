/*document.getElementById("d1").innerHTML="AULA 6";

let nome = Diego //prompt("Digite seu nome");
let idade = 18 //prompt("Digite sua idade");
let ano = 2026;

let nasc = ano-idade;

document.getElementById("resp_ex1").innerHTML= "Olá " + nome + ", seu ano de nascimento é " + nasc;

function alertatop(x){
    alert("Seu nome é: " + x);
}

alertatop(prompt("Digite seu nome: "));


function soma(x,y){
    res = x+y;
    return res;
}

document.getElementById("soma").innerHTML=soma(5,56);*/

let soma = 0;
document.getElementById("incrementado").innerHTML=soma;

function incrementar(){
    let x = Number(document.getElementById("inp1").value);
    soma += x;
    console.log(soma);
    document.getElementById("incrementado").innerHTML=soma;
}