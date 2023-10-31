# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 

area_pintada = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
qtd_latas = round(((area_pintada / 3) / 18) + 0.5)
preco_total = qtd_latas * 80

print("Para pintar {} metros quadrados será necessário {} latas de 18 Litros, ficando no total R$ {}" .format(area_pintada, qtd_latas, preco_total))