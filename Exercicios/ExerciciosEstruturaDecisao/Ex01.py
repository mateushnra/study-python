# Faça um Programa que peça dois números e imprima o maior deles

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

if num1 > num2:
    print("O número {} é maior que o número {}." .format(num1, num2))
else:
    print("O número {} é maior que o número {}." .format(num2, num1))
    