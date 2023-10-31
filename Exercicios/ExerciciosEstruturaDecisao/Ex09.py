# Faça um Programa que leia três números e mostre-os em ordem decrescente. 

n1 = int(input("Informe o valor do primeiro número: "))
n2 = int(input("Informe o valor do segundo número: "))
n3 = int(input("Informe o valor do terceiro número: "))

if n2 < n1 > n3:
    if(n2 > n3):
        print("Ordem decrescente: %d, %d, %d" % (n1,n2,n3))
    else:
        print("Ordem decrescente: %d, %d, %d" % (n1,n3,n2))
elif n1 < n2 > n3:
    if(n1 > n3):
        print("Ordem decrescente: %d, %d, %d" % (n2,n1,n3))
    else:
        print("Ordem decrescente: %d, %d, %d" % (n2,n3,n1))
else:
    if(n1 > n2):
        print("Ordem decrescente: %d, %d, %d" % (n3,n1,n2))
    else:
        print("Ordem decrescente: %d, %d, %d" % (n3,n2,n1))
