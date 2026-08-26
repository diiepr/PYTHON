

while True: 

    try:
        cpf = input("\nDigite um número de CPF (apenas números): ")

        if len(cpf) > 11:
            print("\nUm CPF contém apenas 11 números.")
            continue

        if len(cpf) < 11:
            print("Um CPF válido contém 11 digitos.")
            continue

        cpf = int(cpf)

    except ValueError:
        print("\nIDigite apenas números inteiros.")
        continue



    cpf = str(cpf)
    nove_cpf = cpf[:9]
    soma_dos_numeros = 0
    i = 10
    i_2 = 11

    for numero in nove_cpf:
            soma_dos_numeros += int(numero) * i
            i -= 1

    numero_multiplicado = soma_dos_numeros * 10
    digito_1 = numero_multiplicado % 11

    for numero in nove_cpf:
         soma_dos_numeros += int(numero) * i
         i_2 -= 1

    soma_dos_numeros += digito_1 * 2

    digito_2 = (soma_dos_numeros * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    print(f"\nOs digitos são {digito_1} e {digito_2}")

    cpf_valido = f"{nove_cpf}{digito_1}{digito_2}"

    if cpf == cpf_valido:
         print("CPF é Válido.")
    else:
         print("CPF é inválido.")

        
        
    




