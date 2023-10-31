# Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

letra = input("Informe uma letra e descubra se ela é consoante ou vogal ").upper()

if (letra == 'A') or (letra == 'E') or (letra == 'I') or (letra == 'O') or (letra == 'U'):
    print("É uma vogal")
else:
    print("É uma consoante")
    