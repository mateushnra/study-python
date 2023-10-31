# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: 
    # salários até R$ 280,00 (incluindo) : aumento de 20% 
    # salários entre R$ 280,00 e R$ 700,00 : aumento de 15% 
    # salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% 
    # salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, 
# informe na tela: 
    # o salário antes do reajuste; 
    # o percentual de aumento aplicado; 
    # o valor do aumento; 
    # o novo salário, após o aumento.

salario = float(input("Informe seu salário: "))
salario_antigo = salario
aumento = 0

if salario <= 280: 
    salario *= 1.2
    percent_aplicado = "20%"
    aumento = salario - salario_antigo
elif salario > 280 and salario <= 700:
    salario *= 1.15
    percent_aplicado = "15%"
    aumento = salario - salario_antigo
elif salario > 700 and salario <= 1500:
    salario *= 1.1
    percent_aplicado = "10%"
    aumento = salario - salario_antigo
else:
    salario *= 1.05
    percent_aplicado = "5%"
    aumento = salario - salario_antigo
    
print("O salário atual é R${}, recebeu um aumento de {}, adicionando R${} ao valor antigo do salario R${}" .format(salario, percent_aplicado, aumento, salario_antigo))
