# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
    # comprar apenas latas de 18 litros; 
    # comprar apenas galões de 3,6 litros; 
    # o misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e 

#sempre arredonde os valores para cima, isto é, considere latas cheias. 

area_pintada = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
qtd_litros = area_pintada / 6

#Situação 1: comprar apenas latas de 18 litros
qtd_latas = round((qtd_litros / 18) + 0.5)
preco_total = qtd_latas * 80
print("Apenas utilizando Latas: \nPara pintar {} metros quadrados será necessário {} latas de 18 Litros, ficando no total R$ {}" .format(area_pintada, qtd_latas, preco_total))

#Situação 2: comprar apenas galões de 3,6 litros
qtd_galoes = round((qtd_litros / 3.6) + 0.5)
preco_total = qtd_galoes * 25
print("Apenas utilizando Galões: \nPara pintar {} metros quadrados será necessário {} galões de 3.6 Litros, ficando no total R$ {}" .format(area_pintada, qtd_galoes, preco_total))

#Situação 3: misturar latas e galões e acrescentar 10% de folga
qtd_litros *=  1.1
qtd_latas = qtd_litros / 18
resto_latas = qtd_latas - int(qtd_latas) 
qtd_latas = int(qtd_latas)
qtd_galoes = round(((resto_latas * 18) / 3.6) + 0.5)
preco_total = (qtd_latas * 80) + (qtd_galoes * 25)
print("Utilizando ambos: \nPara pintar {} metros quadrados será necessário {} lata(s) de 18 Litros e {} galãoes de 3.6 Litros, ficando no total R$ {}" .format(area_pintada, qtd_latas, qtd_galoes, preco_total))