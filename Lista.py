
# Exercício que insere, apaga ou lista items de uma lista #

lista = []

import os

while True:
    escolha = input("Selecione uma opção \n[i]nserir  [a]pagar  [l]istar: "  )


    if escolha.startswith("l") and len(lista) == 0:
        os.system("cls")
        print("\nNão existem items para listar.")
        continue
    elif escolha.startswith("l") and len(lista) > 0:
        os.system("cls")
        print("Sua lista: ")
        for i, valor in enumerate(lista, start= int(1)):
            print(i, valor, sep="º ")
            

    elif escolha.startswith("i"):
        os.system("cls")
        lista.append(input("\nDigite um alimento que você deseja adicionar a lista: "))
        print("\nInserido com sucesso!")

    try:
        if escolha.startswith("a"):
            os.system("cls")
            lista.pop(int(input("\nDigite o índice que você deseja apagar: ")))
            print("\nApagado com sucesso!")
    except ValueError:
            print('Por favor digite número int.')
            continue
    except IndexError:
            print('Índice não existe na lista')
            continue
    except Exception:
            print('Erro desconhecido')
            continue
    
        

    