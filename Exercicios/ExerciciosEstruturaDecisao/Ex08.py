# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

prod1 = float(input("Informe valor do primeiro produto: "))
prod2 = float(input("Informe valor do segundo produto: "))
prod3 = float(input("Informe valor do terceiro produto: "))

if prod3 > prod1 < prod2:
    print("O produto 1 é o mais barato, portanto é o que será comprado.")
elif prod1 > prod2 < prod3:
    print("O produto 2 é o mais barato, portanto é o que será comprado.")
else:
    print("O produto 3 é o mais barato, portanto é o que será comprado.")
    