inicial = 1
soma = 1/n
n = 0
final = inicial + soma

x = int(input("Insira um número: "))

while n < x:
    print()
    soma += 1/n
    n += 1

print(1 + soma)