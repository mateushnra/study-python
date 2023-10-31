# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. 

qtd_anos = 0

while True:
    A = float(input("Informe a população da cidade A: "))
    B = float(input("Informe a população da cidade A: "))
    taxaA = float(input("Informe a taxa de crescimento anual da população A: "))
    taxaB = float(input("Informe a taxa de crescimento anual da população B: "))

    if(A > 0 and B > 0 and taxaA > 0 and taxaB > 0):
        break
    else:
        print("A população de A/B e as taxas de crescimento devem ser maior que 0!")

while A <= B:
        A += (A * taxaA) / 100
        B += (B * taxaB) / 100
        qtd_anos += 1
else:
        print("Para a população A ficar maior que B se passaram {} anos" .format(qtd_anos))
