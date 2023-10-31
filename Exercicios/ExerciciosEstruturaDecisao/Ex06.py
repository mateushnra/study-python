# Faça um Programa que leia três números e mostre o maior deles. 

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num3 < num1 > num2:
    print("O número {} é o maior." .format(num1))
elif num1 < num2 > num3:
    print("O número {} é o maior." .format(num2))
else:
    print("O número {} é o maior." .format(num3))
    