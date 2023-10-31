# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F- Feminino, M - Masculino, Sexo Inválido. 

sexo = input("Informe o seu sexo, sendo 'F' para feminino e 'M' para masculino.").upper()

if sexo == 'F':
    print("Feminino")
elif sexo == 'M':
    print("Masculino")
else:
    print("Sexo inválido")
    