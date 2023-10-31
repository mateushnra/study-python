#  Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
      #salário bruto. 
      #quanto pagou ao INSS. 
      #quanto pagou ao sindicato. 
      #o salário líquido. 
      # calcule os descontos e o salário líquido, conforme a tabela abaixo: 
            # + Salário Bruto : R$ 
            # - IR (11%) : R$ 
            # - INSS (8%) : R$ 
            # - Sindicato ( 5%) : R$ 
            # = Salário Liquido : R$ 

#Obs.: Salário Bruto - Descontos = Salário Líquido. 

valor_hora = float(input("Informe quanto você ganha por hora: "))
horas_mes = int(input("Informe a quantidade de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_mes

IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = IR + INSS + sindicato

salario_liquido = salario_bruto - descontos

print("Salário Bruto: R${:.2f}\nDesconto Imposto de Renda: R${:.2f}\nDesconto INSS: R${:.2f}\nDesconto Sindicato: R${:.2f} +\nDesconto Total: R${:.2f}\nSalário Líquido: R${:.2f}".format(salario_bruto, IR, INSS, sindicato, descontos, salario_liquido))