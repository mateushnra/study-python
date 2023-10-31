# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. 

ano = input("Informe um ano: ")
ultimos_digitos = ano[2:]

if (int(ultimos_digitos) % 4) == 0:
    print("Ano bissexto!")
else:
    print("Ano não bissexto!")
    