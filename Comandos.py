# Comandos python, escritos por: WillTechWork
# COMANDOS IF, ELSE, CONDICIONAIS.

# Exemplo abaixo:

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

# ENTRADA DE DADOS EM LINGUAGEM PYTHON:
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

# Exemplo de exercício "LAÇO DE REPETIÇÃO FOR RANGE".

# Laço de repetição, multíplo de 3, FOR in RANGE:
# Nesse caso irei escrever um laço com a contagem do 0 ao 18, sendo que a contagem irá acontecer
# de acordo com o programado e irá pular de casa, de 3 em 3, como deixei claro que irá se repetir em multíplo de 3.

# Obs: Lembrando que se colocarmos de 0 a 18, o laço irá contar até o número 15.

for x in range(0, 18, 3):
    print(x)

# Como podemos ter o entendimento, realizei a programação e quando coloco a função print (x), será mostrado a exibição ao usuário!

# FATIANDO STRINGS

# LOCALIZANDO O ÍNDICE:
# 012345, esse conceito de indexação, é de acordo com a norma para localização de índice.
# Quando desejamos imprimir uma string de trás pra frente, no caso o (n), realizamos da seguinte forma:

# EXEMPLO:
# -1 = n, -2 = o, -3 = h, - 4 = t, -5 = y, -6 = p

# NESSE CASO IREMOS ESCREVER: Python

nome = 'python'  # Assim, como podemos ver, criei uma string chamada: Python.
# Criando uma nova variável para localizar a string. Ficaria assim: nova_string = nome + [] < dentro dos colchetes a posição do índice.
nova_string = nome[-6]
print(nova_string)


# INSTRUÇÃO BREAK COTINUE, EXPLICAÇÃO:

# Aqui, acontece que irei utilizar o print, para mostrar ao usuário a forma de entrar no laço, após criar o range e assim determinando até o 10.
# Após, criei a "CONDIÇÃO", para quando chegar ao numeral 5, consequentemente parar no número 5.
# Entrando no laço, "EXEMPLO ABAIXO":

print("Entrando no laço...")
for i in range(10):
    print(i)
    if (i == 5)
    break
    print("Saindo do laço...")
