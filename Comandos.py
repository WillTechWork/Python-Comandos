# Comandos python, escritos por: WillTechWork
# Comando if, Else, condicionais.

#Exemplo abaixo: 

# O comando if = se, se a condição for verdadeira, ou seja, #True, ela será executada em seguida!
# O comando else = senão, se a condição for falsa, ou seja, #False, essa condição será executada em segunda condição!
numero = 10

if numero == 10:  # True, Se
    print("Este número é igual a 10!")
else:  # False, Senão
    print("Este número não é igual a 10!")

# Agora irei escrever os comandos de sintaxe de comparação.
# O comando print, mostra o conteúdo que irá apresentar ao usuário.

print("a" == "b")
print("b" != "a")
print("a" > "x")
print("a" > "1")

# A linguagem python se baseia na linguagem ASCII

for i in range(122):
    print(str(i) + " -"+chr(i))

# Entrada de Dados em Python!
# O comando input (), permite que o usuário adicione dados, assim permitindo a entrada de dados!
# Vamos alocar o comando input dentro de uma variável!
nome = input("Digite o seu nome: ")  # Tipo string
idade = int(input("Digite a sua idade: "))  # inteiro
peso = float(input("Digite o seu peso: "))  # float

print("'Meu nome é: ", nome, ", minha idade é: ",
      idade, "e o meu peso é de:", peso, "Kg'")


# Exemplo de exercício "CONDICIONAL".

numero = 15

if numero == 15:  
    print("Este número é igual a 15!")
elif numero > 15:
    print("Este número é maior que 15!")
elif numero < 15:
    print("Este número é menor que 15!")



