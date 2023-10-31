# Faça um programa que leia e valide as seguintes informações: 
    # Nome: maior que 3 caracteres; 
    # Idade: entre 0 e 150; 
    # Salário: maior que zero; 
    # Sexo: 'f' ou 'm'; 
    # Estado Civil: 's', 'c', 'v', 'd'; 

while True:
    nome = input("Informe o seu nome: ")

    if(len(nome) > 3):
        break
    else:
        print("O seu nome deve possuir mais de 3 caracteres!")
        
while True:    
    idade = int(input("Informe a sua idade: "))

    if(idade >= 0 and idade <= 150):
      break
    else:
      print("A sua idade deve estar entre 0 a 150!")  

while True:
    salario = float(input("Informe o seu salário: "))

    if(salario > 0):
      break
    else:
      print("O seu salário deve ser maior que 0!")  

while True:
    sexo = input("Informe o seu sexo:\nf - Feminino\nm - Masculino ").lower()

    if(sexo == 'f' or sexo == 'm'):
        break
    else:
        print("O seu sexo deve ser f (Feminino) ou m (Masculino)!")

while True:
    estadoCivil = input("Informe o seu estado civil:\ns - Solteiro(a)\nc - Casado(a)\nv - Viuvo(a)\nd - Divorciado(a) ").lower()

    if(estadoCivil == 's' or estadoCivil == 'c' or estadoCivil == 'v' or estadoCivil == 'd'):
        break
    else:
        print("O seu estado civil deve ser respectivamente uma das seguintes opções: s (Solteiro(a)), c (Casado(a)), v (Viuvo(a)) e d (Divorciado(a))")
        