# Exercicio 1 - Manipulação de Strings

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


try:
    print(f'Seu nome é {nome}')
    print(f"Seu nome invertido é {nome[::-1]}")

    if " " in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços.")

    print(f'Seu nome tem {len(nome)} letras')
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
except ValueError:
    print("Você deixou campos vazios.")
    
 
    



      