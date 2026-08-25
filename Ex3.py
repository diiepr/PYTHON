# Exercício que adiciona caracteres e transforma o nome #

nome = input("Digite o seu nome: ")
qntd_letras = len(nome)
cont = 0
novo_nome = ''

while cont < qntd_letras:
    novo_nome += f"*{nome[cont]}"
    cont += 1

print(f"Novo nome: {novo_nome}")



