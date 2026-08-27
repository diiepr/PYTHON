# Calculadora com While #

while True:

    float_numero_1 = 0
    float_numero_2 = 0

    numero_1  = input("Digite um número: ")
    numero_2 =  input("\nDigite outro número: ")
    numeros_validos = None


    try:
        float_numero_1 = float(numero_1)
        float_numero_2 = float(numero_2)
        numeros_validos = True
    except ValueError:
        numeros_validos = None

    if numeros_validos is None:
        print("\nUm ou ambos os números estão incorretos.")
        continue

    
    operacao = input("\nDigite uma operação [+][-][*][/]: ")
    operacao_valida = "+-*/"


    while len(operacao) > 1:
        print("\nDigite apenas um operador.")
        operacao = input("\nDigite uma operação [+][-][*][/]: ")
        continue

    while operacao not in operacao_valida:
        print("\nOperação Inválida.")
        operacao = input("\nDigite uma operação [+][-][*][/]: ")
        continue

   



    if operacao == "+":
        soma  = float_numero_1 + float_numero_2
        print(f"\nSoma: {soma}")
    elif operacao == "-":
        subtracao = float_numero_1 - float_numero_2
        print(f"\nSubtração: {subtracao}")
    elif operacao == "*":
        multiplicacao = float_numero_1 * float_numero_2
        print(f"\nMultiplicação: {multiplicacao}")
    else:
        divisao = float_numero_1 / float_numero_2
        print(f"\nDivisão: {divisao}")

    sair = input("\nQuer sair?  [s]im: ")
    sair = sair.lower().startswith("s")
    
    if sair is True:
        break

            


