# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
    # "Telefonou para a vítima?" 
    # "Esteve no local do crime?" 
    # "Mora perto da vítima?" 
    # "Devia para a vítima?" 
    # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 

classificacao = 0

print("Digite as respectivas respostas para as perguntas abaixo:\n\n" +
      "S - caso afirmativo\n" +
      "N - caso negativo")

if input("Telefonou para a vítima? ").upper() == 'S': classificacao += 1 
if input("Esteve no local do crime? ").upper() == 'S': classificacao += 1 
if input("Mora perto da vítima? ").upper() == 'S': classificacao += 1 
if input("Devia para a vítima? ").upper() == 'S': classificacao += 1 
if input("Já trabalhou com a vítima? ").upper() == 'S': classificacao += 1 

match classificacao:
    case 2:
        print("Suspeita")
    case 3:
        print("Cúmplice!")
    case 4:
        print("Cúmplice!")
    case 5:
        print("Assassino!")
    case _:
        print("Inocente")
