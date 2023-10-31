# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento

num = float(input("Informe um número: "))

if(round(num) == num):
    print("O número {} é inteiro!".format(num))
else:
    print("O número {} é decimal!".format(num))
    