# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina. 
    # Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1; 
    # Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("Informe um valor inteiro a ser sacado: "))
saqueStr = str(saque)
qtd_100 = 0
qtd_50 = 0
qtd_10 = 0
qtd_5 = 0
qtd_1 = 0

if saque >= 10 and saque < 100:
    dezenas = int(saqueStr[0])
    if(dezenas >= 5):
        qtd_50 += 1
        dezenas -= 5
    qtd_10 += dezenas
    
    unidades = int(saqueStr[1])
    if(unidades >= 5):
        qtd_5 += 1
        unidades -= 5
    qtd_1 += unidades
elif(saque >= 100 and saque <= 600):
    qtd_100 += int(saqueStr[0])

    dezenas = int(saqueStr[1])
    if(dezenas >= 5):
        qtd_50 += 1
        dezenas -= 5
    qtd_10 += dezenas
    
    unidades = int(saqueStr[2])
    if(unidades >= 5):
        qtd_5 += 1
        unidades -= 5
    qtd_1 += unidades
else:
    print("Valor informado não cumpre os requisitos. Valor mínimo a ser sacado é de 10 reais e o máximo 600 reais!")

print("Quantidade de notas recebidas:",
      "\nNotas de 100: ", qtd_100,
      "\nNotas de 50: ", qtd_50,
      "\nNotas de 10: ", qtd_10,
      "\nNotas de 5: ", qtd_5,
      "\nNotas de 1: ", qtd_1)
