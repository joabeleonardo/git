total = 0
numero = 1
while numero != 0:
    numero = int(input("Informe um número inteiro: "))
    total = total + numero

print(f"A soma dos números digitados é {total}")

#####
alvo = int(input("Informe um número"))

for item in range(1,alvo+1,1):
    print(item)
