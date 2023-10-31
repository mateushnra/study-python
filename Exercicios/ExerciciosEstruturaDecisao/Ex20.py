# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: 
    # A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada; 
    # A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada; 
    # A mensagem "Aprovado com Distinção", se a média for igual a 10. 

nota1 = float(input("Informe a sua primeira nota: "))
nota2 = float(input("Informe a sua segunda nota: "))
nota3 = float(input("Informe a sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media < 10:
    print("Aprovado com media %d"%(media))
elif media >= 0 and media < 7:
    print("Reprovado com media %d"%(media))
elif media == 10:
    print("Aprovado com Distinção!")
else:
    print("Uma ou mais notas informadas estão fora do esperado (0 a 10)")
