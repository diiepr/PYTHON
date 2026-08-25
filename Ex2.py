# exercícios variados utilizando try/except #

try:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print("\nSeu número é par.")
    else:
        print("\nSeu número é ímpar")
except ValueError:
        print("\nIsso não é um número inteiro.")




try:
     nome = input("\nDigite o seu nome: ")
     horario = int(input("\nDigite o horário: "))
     if horario >= 0 and horario <= 11:
          print(f"Bom dia, {nome}!\n")
     elif horario > 11 and horario <= 17:
          print(f"Boa tarde, {nome}!\n")
     elif horario > 17 and horario <= 23:
          print(f"Boa noite, {nome}!\n")
     else:
          print("Não conheço essa hora.")
except ValueError:
     print("Horário inválido")



try:
     nome = input("\nDigite o seu primeiro nome: ")
     tamanho_nome = len(nome)
     if tamanho_nome > 0 and tamanho_nome <= 4:
          print("\nSeu nome é curto.")
     elif tamanho_nome > 4 and tamanho_nome <= 6:
          print("\nSeu nome é normal.")
     else:
          print("\nSeu nome é  grande.")
except ValueError:
     print("\nIsso não é um nome.")



        
        