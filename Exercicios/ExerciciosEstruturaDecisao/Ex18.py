# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 

data = input("Informe uma data no formato dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

if dia <= 31 and mes <= 12 and ano > 0:
    print("Data válida!")
else:
    print("Data inválida!")
