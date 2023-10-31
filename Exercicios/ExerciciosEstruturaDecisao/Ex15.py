# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
# Dicas: 
    # Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; 
    # Triângulo Equilátero: três lados iguais; 
    # Triângulo Isósceles: quaisquer dois lados iguais; 
    # Triângulo Escaleno: três lados diferentes;

A = float(input("Informe o valor do primeiro lado do triângulo: "))
B = float(input("Informe o valor do segundo lado do triângulo: "))
C = float(input("Informe o valor do terceiro lado do triângulo: "))

if ((A + B) > C) and ((A + C) > B) and ((B + C) > C):
    if A == B == C:
        print("Triângulo Equilátero")
    elif A == B or A == C or B == C:
        print("Triângulo Isósceles")
    elif A != B and A != C and B != C:
        print("Triângulo Escaleno")
else:
    print("De acordo com as medidas o lados informados não correspondem a um triângulo!")
