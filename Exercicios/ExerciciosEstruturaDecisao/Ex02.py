# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("Informe um número e descubra se ele é positivo ou negativo: "))

if num < 0:
    print("O número {} é negativo." .format(num))
else:
    print("O número {} é positivo." .format(num))
    