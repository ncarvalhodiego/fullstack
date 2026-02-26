"""a = int(10)
b = int(15)
c = int(24)
if (a<b+c) and (b<a+c) and (c<a+b):
    if (a==b)and(b==c):
        print("Triangulo equilatero")
    else:
        if (a==b)or(b==c):
            print("Triangulo isosceles")
        else:
            print("Triangulo escaleno")
else:
    print("Nao e um triangulo")
"""
preço = float(input("Digite o preço:"))
codigo = int(input("Digite o código de origem:"))
origem = str("")

if codigo == 1:
    origem = "Sul"
elif codigo == 2:
    origem = "Norte"
elif codigo == 3:
    origem = "Leste"
elif codigo == 4:
    origem = "Oeste"
elif codigo >= 5 or codigo <= 6:
    origem = "Nordeste"
elif codigo >= 7 and codigo <= 9:
    origem = "Sudeste"
elif codigo >= 10 and codigo <= 20:
    origem = "Centro-Oeste"
elif codigo >= 25 and codigo <= 30:
    origem = "Noroeste"
else:
    origem = "Importado"
print("R$", preço,"-", origem)