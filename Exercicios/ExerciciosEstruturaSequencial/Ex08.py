# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

val_hora = float(input("Informe quanto você ganha por hora: "))
horas_mes = int(input("Informe quantas horas você trabalha no mês: "))

print("Seu salário mensal é de R$ {}".format((val_hora * horas_mes)))
