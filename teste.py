"""
📘 Exercício 5: Menu interativo simples
Objetivo: Criar um loop com múltiplas opções.
Descrição: Monte um menu que mostra opções como:
1 - Dizer "Olá"
2 - Dizer "Tchau"
3 - Sair
O programa só para quando o usuário escolher a opção 3.

"""

menu = int(input("1 = Olá | 2 = Tchau | 3 = Sair: "))

while menu != 3:
    if menu == 1:
        print("Olá")
    elif menu == 2:
        print("Tchau")
    else:
        print("Opção inválida. Tente novamente.")
    
    menu = int(input("1 = Olá | 2 = Tchau | 3 = Sair: "))

print("Saindo... até logo!")
