
nome = input("Olá, sou o ChatBot e vou ajudar. Qual o seu nome? ")
print(f"Seja Bem-vindo {nome}")

#laço de repetição
while True:
    print("\nChatBot Selecione uma opção: ")
    print("1 - Fiscal")
    print("2 - Pessoal")
    print("3 - Contábil")
    print("4 - Suporte")
    print("5 - Sair")

    opcao = input().strip() #tirar espaços

    if opcao == "1": #quando usar o input pegamos uma informação, o usuário sempre retorna com texto, por isso as aspas
        fiscal = "Espere um instante que você esta sendo direcionado para o setor Fiscal"
        print(fiscal)
    elif opcao == "2":
        pessoal = "Espere um instante que você esta sendo direcionado para o setor Pessoal"
        print(pessoal)
    elif opcao == "3":
        contabil = "Espere um instante que você esta sendo direcionado para o setor Contábil"
        print(contabil)
    elif opcao == "4":
        suporte = "Espere um instante que você esta sendo direcionado para o Suporte"
        print(suporte)
    elif opcao == "5":
        print(f"Até mais {nome} (tchau)")
        break #break serve para quebrar o laço de repetição, se caso não colocasse ele aqui iria repetir o print das seleções de opções
    else:
        print("Desculpe não entendi, escolha uma opção de 1 a 5.")
