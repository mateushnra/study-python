# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

while True:
    usuario = input("Informe seu usuario: ")
    senha = input("Informe a sua senha: ")

    if(usuario != senha):
        break
    else: 
        print("A senha não pode ser igual ao nome de usuário!")
