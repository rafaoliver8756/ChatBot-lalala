import random


nome = input("Olá, sou o ChatBot e vou ajudar. Qual o seu nome? ")
print(f"Seja Bem-vindo {nome}")

#laço de repetição
while True:
    print("\nChatBot Selecione uma opção: ")
    print("1 - Piadas")
    print("2 - Frase do dia")
    print("3 - Adivinha")
    print("4 - Sair")

    opcao = input().strip() #tirar espaços

    if opcao == "1": #quando usar o input pegamos uma informação, o usuário sempre retorna com texto, por isso as aspas
        piadas = ["vcaaaaaaaaaaaaaaaaaa", "slaaaaaaaaa", "aquiaaaaaaa"]
        print(random.choice(piadas))
    elif opcao == "2":
        frases = ["faaaaaaaa", "caaaaaaaaa", "baaaaaaaaaa"]
        print(random.choice(frases))
    elif opcao == "3":
        adivinha = ["saaaaaa", "haaaaaaa", "yaaaaaaaaa"]
        print(random.choice(adivinha))
    elif opcao == "4":
        print(f"Até mais {nome} (tchau)")
        break #break serve para quebrar o laço de repetição, se caso não colocasse ele aqui iria repetir o print das seleções de opções
    else:
        print("Desculpe não entendi, escolha uma opção de 1 a 4.")
