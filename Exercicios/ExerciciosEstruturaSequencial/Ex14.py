# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multao valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Informe o peso total dos peixes pescados: "))
excesso = (peso - 50) * 4

print("O peso dos peixes pescados por João é de {} quilos. O valor da multa que deverá ser pago por quilo excedente é R${}" .format(peso, excesso))