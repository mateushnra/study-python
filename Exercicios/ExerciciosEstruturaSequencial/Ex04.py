# Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

nota1 = float(input("Informe a sua primeira nota bimestral: "))
nota2 = float(input("Informe a sua segunda nota bimestral: "))
nota3 = float(input("Informe a sua terceira nota bimestral: "))
nota4 = float(input("Informe a sua quarta nota bimestral: "))

print("A sua nota final: {}".format(round(((nota1 + nota2 + nota3 + nota4) / 4),1)))
