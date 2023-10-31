# Uma fruteira está vendendo frutas com a seguinte tabela de preços: 

# Morango:
    #Até 5 Kg: R$ 2,50 por Kg
    #Acima de 5Kg: R$ 2,20 por KG

# Maçã:
    #Até 5 Kg: R$ 1,80 por Kg
    #Acima de 5Kg: R$ 1,50 por KG

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 

qtd_kg_morango = float(input("Informe a quantidade em kg de morango que você irá comprar: "))
qtd_kg_maca = float(input("Informe a quantidade em kg de maça que você irá comprar: "))

total_kg = qtd_kg_morango + qtd_kg_maca

total_valor = qtd_kg_morango * 2.5 if qtd_kg_morango <= 5 else qtd_kg_morango * 2.2
total_valor += qtd_kg_maca * 1.8 if qtd_kg_maca <= 5 else total_valor + qtd_kg_maca * 1.5

if total_kg > 8 or total_valor > 25: total_valor *= 0.9

print("Valor total da compra: R$ {:.2f}" .format(total_valor))
