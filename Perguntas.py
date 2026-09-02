# Perguntas

import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': [1, 3, 4, 5],
        'Resposta': 4,
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': [25, 55, 10, 51],
        'Resposta': 25,
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': [4, 5, 2, 1],
        'Resposta': 5,
    },
    {
        'Pergunta': 'Quem descobriu o Brasil?',
        'Opções': ["Pedro Alvarez Cabral", "Cristóvão Colombo", "Vasco da Gama", "Fernando de Magalhães"],
        'Resposta': "Pedro Alvarez Cabral",
    }
]
qnt_acertos = 0
for pergunta in perguntas:
    os.system("cls")
    print("\n" + pergunta['Pergunta'] + "\n")
    for i, opcao in enumerate(pergunta['Opções']):
        print(f"{i + 1}. {opcao}")

    while True:
        escolha = input("Escolha uma opção: ")

        try:
            escolha = int(escolha)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if escolha < 1 or escolha > len(pergunta['Opções']):
            print("Opção inválida. Tente novamente.")
            continue

        if pergunta['Opções'][escolha - 1] == pergunta['Resposta']:
            qnt_acertos += 1  
            break  
        else:
            break

print(f"\nVocê acertou {qnt_acertos} de {len(perguntas)} perguntas.")

