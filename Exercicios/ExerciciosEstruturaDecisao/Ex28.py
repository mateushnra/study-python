# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira: 

# File Duplo:
    #Até 5 Kg: R$ 4,90 por Kg
    #Acima de 5Kg: R$ 5,80 por KG

# Alcatra:
    #Até 5 Kg: R$ 5,90 por Kg
    #Acima de 5Kg: R$ 6,80 por KG

# Picanha:
    #Até 5 Kg: R$ 6,90 por Kg
    #Acima de 5Kg: R$ 7,80 por KG

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

carne = int(input("Informe qual tipo de carne você deseja comprar:\n\n1 - File Duplo\n2 - Alcatra\n3 - Picanha"))
qtd_kg_carne = float(input("Informe a quantidade de carne que você deseja comprar em kg: "))
pagamento = int(input("Informe o método de pagamento:\n\n1 - Cartão Tabajara\n2 - Outro método de pagamento"))

opValido = True

match carne:
    case 1:
        carne = "File Duplo"
        total = qtd_kg_carne * 4.9 if qtd_kg_carne <= 5 else qtd_kg_carne * 5.8
    case 2:
        carne = "Alcatra"
        total = qtd_kg_carne * 5.9 if qtd_kg_carne <= 5 else qtd_kg_carne * 6.8
    case 3:
        carne = "Picanha"
        total = qtd_kg_carne * 6.9 if qtd_kg_carne <= 5 else qtd_kg_carne * 7.8
    case _:
        print("Carne informada inválida!")
        opValido = False

if(opValido):
    match pagamento:
        case 1:
            pagamento = "Cartão Tabajara"
            desconto = total * 0.05
            total_pagar = total * 0.95
        case 2:
            pagamento = input("Informe qual será o método de pagamento: ")
            desconto = 0
            total_pagar = total
        case _:
            print("Método de pagamento inválido")
            opValido = False

if  opValido:
    print("CUPOM FISCAL\n\nCarne: {}\nQuantidade: {}\nValor Total: {:.2f}\nPagamento: {}\nValor do desconto: {:.2f}\nValor Final: {:.2f}".format(carne, qtd_kg_carne, total, pagamento, desconto, total_pagar))
    