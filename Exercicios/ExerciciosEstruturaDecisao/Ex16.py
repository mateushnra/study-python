#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações: 
    # a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado; 
    # b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa; 
    # c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário; 
    # d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 

a = float(input("Informe o valor de A da equação de 2° grau: "))
b = float(input("Informe o valor de B da equação de 2° grau: "))
c = float(input("Informe o valor de C da equação de 2° grau: "))

delta = a**2 - 4*a*c

xPositivo = ((-b) + delta ** 0.5) / (2 * a)
xNegativo = ((-b) - delta ** 0.5) / (2 * a)

if a == 0:
    print("A equação não é de segundo grau, informe um valor diferente de 0 para A.")
elif delta < 0:
    print("O equação não possui raizes reais.")
elif delta == 0:
    print("Existe apenas uma raiz real, e seu valor é {}." .format(xPositivo) )
else:
    print("Existem duas raizes reais, a raiz positiva é {} e a negativa é {}.".format(xPositivo, xNegativo))
    