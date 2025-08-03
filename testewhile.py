"""
🧪 Exercícios Básicos com while
📘 Exercício 1: Contagem simples
Objetivo: Praticar repetição com controle de variável.
Descrição: Escreva um programa que imprima os números de 1 a 10 usando while.
"""
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

"""
📘 Exercício 2: Somando números
Objetivo: Usar entrada do usuário em um laço while.
Descrição: O programa deve pedir números ao usuário até que ele digite 0. Ao final, mostrar a soma de todos os números digitados.

"""
soma = 0
numero = int(input("Digite um número para somar (0 para sair): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número (0 para sair): "))

print(f"O resultado é {soma}")

"""
📘 Exercício 3: Validação de senha
Objetivo: Praticar verificação de condição dentro do laço.
Descrição: Peça para o usuário digitar uma senha até que ele digite a senha correta ("python123").

"""
senha = input("Digite a senha para entrada: ")

while senha != "python123":
    senha = input("Senha incorreta, digite novamente: ")

print("Você entrou.")


"""
📘 Exercício 4: Contador regressivo
Objetivo: Trabalhar decremento dentro do laço.
Descrição: Peça ao usuário um número inteiro positivo e faça uma contagem regressiva até 0.

"""

numero = int(input("Digite um número inteiro para verificar seu decremento:"))

while numero >= 0:
    print(numero)
    numero -= 1
    
"""
📘 Exercício 5: Menu interativo simples
Objetivo: Criar um loop com múltiplas opções.
Descrição: Monte um menu que mostra opções como:
1 - Dizer "Olá"
2 - Dizer "Tchau"
3 - Sair
O programa só para quando o usuário escolher a opção 3.

"""

menu = int(input(" 1 = Olá : 2 = Tchau : 3 = Sair"))
    