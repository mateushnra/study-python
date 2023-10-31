# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe um número inteiro: "))
n3 = float(input("Informe um número real: "))

print(f"A. {((n1*2) * (n2/2))}")
print(f"B. {((n1*3) + n3 )}")
print(f"C. {pow(n3,3)}")