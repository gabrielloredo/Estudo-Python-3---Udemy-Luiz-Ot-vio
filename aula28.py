nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
espaço = " "

if nome and idade != " ":
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if  espaço in nome:
        print("Seu nome contém espaço")
    else:
        print("Não contém espaços")

    print(f"Seu nome  tem {len(nome)} letras.")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A primeira letra do seu nome é {nome[-1]}")

else:
    print("Desculpe, você deixou campos vazios.")


