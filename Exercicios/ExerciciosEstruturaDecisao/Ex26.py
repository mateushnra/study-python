# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool: 
    #até 20 litros, desconto de 3% por litro 
    #acima de 20 litros, desconto de 5% por litro 
# Gasolina: 
    #até 20 litros, desconto de 4% por litro 
    #acima de 20 litros, desconto de 6% por litro 

#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input("Informe com qual combustível você deseja abastecer sendo:\n\n" +
                    "A - Álcool\n" +
                    "G - Gasolina").upper()

qtd_abastecer = float(input("Informe a quantidade que será abastecida: "))

if combustivel == 'A' or combustivel == "G":
    if qtd_abastecer > 0 and qtd_abastecer <= 20 :
        total = qtd_abastecer * (1.9 * 0.97) if combustivel == 'A' else qtd_abastecer * (2.5 * 0.96)
        print("O custo total para abastecer seu veículo ficou R$ {}".format(total))
    elif qtd_abastecer > 20:
        total = qtd_abastecer * (1.9 * 0.95) if combustivel == 'A' else qtd_abastecer * (2.5 * 0.94)
        print("O custo total para abastecer seu veículo ficou R$ {}".format(total))
    else:
        print("A quantidade de combustível não pode ser negativa!")
else:
    print("Combustível inválido!")
