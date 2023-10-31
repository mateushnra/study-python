# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. 
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo: 
    # 326 = 3 centenas, 2 dezenas e 6 unidades 
    # 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 

num = int(input("Informe um número inteiro menor que 1000: "))
numStr = str(num)
mensagem = numStr[0]

if num < 10 and num >= 0:
    mensagem += " unidades"  
    if num == 1:
        mensagem = mensagem.replace("unidades", "unidade")
elif num < 100 and num >= 10:
    mensagem += " dezenas"
    if int(numStr[0]) == 1:
        mensagem = mensagem.replace("dezenas", "dezena")

    mensagem += " e " + numStr[1] + " unidades"  
    if int(numStr[1]) == 1:
        mensagem = mensagem.replace("unidades", "unidade")
elif num < 1000 and num >= 100:
    mensagem += " centenas"
    if int(numStr[0]) == 1:
        mensagem = mensagem.replace("centenas", "centena")

    mensagem += ", " + numStr[1] + " dezenas"
    if int(numStr[1]) == 1:
        mensagem = mensagem.replace("dezenas", "dezena")

    mensagem += " e " + numStr[2] + " unidades"  
    if int(numStr[2]) == 1:
        mensagem = mensagem.replace("unidades", "unidade")
else: 
    print("O número informado deve ser de 0 a 999!")

print(mensagem)
