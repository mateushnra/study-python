# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é: 
    # par ou ímpar; 
    # positivo ou negativo; 
    # inteiro ou decimal. 

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
op = int(input("Informe a operação que você deseja realizar:\n\n" +
               "1 - Adição\n" +
               "2 - Subtração\n" +
               "3 - Multiplicação\n" +
               "4 - Divisão"))

opValido = True

match op:
    case 1: 
        resultado = num1 + num2  
    case 2:
        resultado = num1 - num2  
    case 3:
        resultado = num1 * num2 
    case 4:
        resultado = num1 / num2   
    case _:
        print("Valor de operação informado inválido")
        opValido = False

if(opValido):
    parImpar = "par" if resultado % 2 == 0 else "ímpar"
    positivoNegativo = "negativo" if resultado < 0 else "positivo"
    intDec = "inteiro" if round(resultado) == resultado else "decimal"

    print("O resultado da operação é {}, sendo um numero {}, {} e {}." .format(resultado, parImpar, positivoNegativo, intDec))
    