n1 = int(input("Primeiro Número:"))
n2 = int(input("Segundo Número:"))
n3 = int(input("Terceiro Número:"))

Primeiro = int(0)
Segundo = int(0)
Terceiro = int(0)

if n1 > n2 and n2 > n3:
    #print("s1")
    Primeiro = n1
    Segundo = n2
    Terceiro = n3
elif n1 > n2 and n3 > n2 and n1 > n3:
    #print("s2")
    Primeiro = n1
    Segundo = n3
    Terceiro = n2
elif n2 > n1 and n1 > n3 and n2 > n3:
    #print("s3")
    Primeiro = n2
    Segundo = n1
    Terceiro = n3
elif n2 > n1 and n3 > n1 and n2> n3:
    #print("s4")
    Primeiro = n2
    Segundo = n3
    Terceiro = n1
elif n3 > n1 and n1 > n2 and n3 > n2:
    #print("s5")
    Primeiro = n3
    Segundo = n1
    Terceiro = n2
elif n3 > n2 and n2 > n1 and n3 > n1:
    #print("s6")
    Primeiro = n3
    Segundo = n2
    Terceiro = n1
"""elif n1 == n2 and n1 > n3:
    #print("s7")
    Primeiro = n1  
    Segundo = n2
    Terceiro = n3
elif n1 == n2 and n3 > n1:
    #print("s8")
    Primeiro = n3 
    Segundo = n1
    Terceiro = n2
elif n2 == n3 and n2 > n1:
    #print("s9")
    Primeiro = n2
    Segundo = n3
    Terceiro = n1
elif n2 == n3 and n1 > n2:
    #print("s10")
    Primeiro = n1
    Segundo = n2
    Terceiro = n3
elif n1 == n3 and n1 > n2:
    #print("s11")
    Primeiro = n1  
    Segundo = n3
    Terceiro = n2
elif n1 == n3 and n2 > n1:
    #print("s12")
    Primeiro = n2
    Segundo = n3
    Terceiro = n1
elif n1 == n2 and n2 == n3:
    #print("s13")
    Primeiro = n1
    Segundo = n2
    Terceiro = n3"""
else: print("DEU ERRO")

print(Primeiro, Segundo, Terceiro)