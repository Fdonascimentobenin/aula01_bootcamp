# Usando o Print
print("Bom dia turma do Bootcamp!")

print(3 + 5)

print("Olá" + " " + "Turma" + " " + "a aula 01" + " " + "começou")

# Usando o input
print(input("Digite seu nome: "))

print("Olá, " + input("Digite seu nome: ") + "!")


## Crie programa que o usuário digita o seu nome e retorna o número de caracteres
print(len(input("Digite seu nome: ")))

## Criar um programa onde o usuário digite dois valores e apareça a soma
print(int(input("Digite o primeiro numero: ")) + int(input("Digite o segundo numero: ")))

# Variaveis e seus tipos de dados
numero = 3 # int
print(type(numero))
numero_decimal = 4.78 # Float
nome_usuario = "Felipe" # String
verdadeiro = True # bool

## Refatore o exercicio anterior atribuindo variaveis
nome = input("Digite o seu nome: ")
quant_caracteres = len(nome)
print(quant_caracteres)

