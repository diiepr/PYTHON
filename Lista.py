
# Exercício que insere, apaga ou lista items de uma lista #

lista = []

import os

while True:
    escolha = input("Selecione uma opção \n[i]nserir  [a]pagar  [l]istar: "  )


    try:
        if escolha.lower().startswith("a"):
            os.system("cls")
            lista.pop(int(input("\nDigite o índice que você deseja apagar: ")))
            
    except ValueError:
            print('Por favor digite número int.')
            continue
    except IndexError:
            print('Índice não existe na lista')
            continue
    except Exception:
            print('Erro desconhecido')
            continue


    if escolha.lower().startswith("l") and len(lista) == 0:
        os.system("cls")
        print("\nNão existem items para listar.")
        continue


    elif escolha.lower().startswith("l") and len(lista) > 0:
        os.system("cls")
        print("Sua lista: ")
        for i, valor in enumerate(lista, start= int(1)):
            print(i, valor, sep="º ")
            

    elif escolha.lower().startswith("i"):
        os.system("cls")
        lista.append(input("\nDigite um alimento que você deseja adicionar a lista: "))
        print("\nInserido com sucesso!")

    elif escolha.lower().startswith("a"):
         continue


    else:
         os.system("cls")
         print("Digite apenas i, a ou l.")
         continue

    

    
    
        

    