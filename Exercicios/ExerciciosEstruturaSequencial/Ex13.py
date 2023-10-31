# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
# Para homens: (72.7*h) - 58 
# Para mulheres: (62.1*h) - 44.7 

h = float(input("Informe a sua altura: "))

pesoIdealHomem = (72.7 * h) - 58
pesoIdealMulher = (62.1 * h) - 44.7

print("O peso ideal para alguém de {} de altura é:\nHomem - {:.2f} kg\nMulher - {:.2f} kg" .format(h, pesoIdealHomem, pesoIdealMulher))
