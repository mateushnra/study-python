# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

diaSemana = int(input("Informe o dia da semana:\n\n" +
                   "1 - Domingo\n" +
                   "2 - Segunda-feira\n" + 
                   "3 - Terça-feira\n" +
                   "4 - Quarta-feira\n" +
                   "5 - Quinta-feira\n" +
                   "6 - Sexta-feira\n" +
                   "7 - Sábado"))

match diaSemana:
    case 1:
        print("Hoje é domingo!")
    case 2:
        print("Hoje é segunda-feira!")
    case 3: 
        print("Hoje é terça-feira!")
    case 4: 
        print("Hoje é quarta-feira!")
    case 5: 
        print("Hoje é quinta-feira!")
    case 6: 
        print("Hoje é sexta-feira!")
    case 7: 
        print("Hoje é sábado!")
    case _:
        print("Valor informado inválido!")
