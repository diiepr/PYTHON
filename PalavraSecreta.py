# Jogo da palavra secreta #

palavra_secreta  = "diego"
tentativas = 0
letras_acertadas = ""

import os

while True:

    letra_digitada = input("Digite uma letra e eu mostrarei se está presente na palavra secreta: ")
    tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""

    for letras in palavra_secreta:
        if letras in letras_acertadas:
            palavra_formada += letras
        else:
            palavra_formada += "*"

    print(palavra_formada)

    if palavra_formada == palavra_secreta:

        os.system("cls")
        print("Parábens, você ganhou o jogo após", tentativas, "tentativas!")
        print("\nAgora tente você, crie uma palavra secreta.")
        palavra_secreta = input("Digite a palavra secreta: ")
        tentativas = 0
        letras_acertadas = ""
        os.system("cls")

    




    
