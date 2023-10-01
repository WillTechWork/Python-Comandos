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

# Outro exemplo, mas com a condicional WHILE, em português = ENQUANTO.

print("Entrando no laço")  # Entrando no laço.
i = 0  # Criei uma variável, atributo i = 0, afirmando que i é = 0.
# Enquanto (i) for menor que (10), dessa forma irá realizar a contagem.
while (i < 10):
    # Agora irei realizar o condicionamento de incremento adicionando + 1.
    i += 1
    # Agora nesse momento determino que (i) terá o resto da divisão dividido por 2, todo número que irá resultar em (número par), dessa forma, será ignorado números pares.
    # Quando for realizar a impressão, mostrará apenas os números ímpares. O comando continue, ele irá ignorar determinada condição e assim irá continuar o fluxo.
    if (i % 2 == 0):
        # Imprimo o resultado para o usuário, assim consequentemente aparece: 1, 3, 5, 7 e 9.
        print(i)
        # Imprimindo ao usuário a saída do laço
        print("Saindo do laço...")


# MANIPULANDO STRINGS COM PYTHON, EXEMPLO:
# Criando variáveis e atribuindo strings.

Nome = "Willian"

# OBS: Podemos declarar "STRINGS", tanto com aspas duplas ou aspas simples!
# STRINGS: É menos que uma lista de caracteres, pode ser nome, textos e etc.

Nome2 = "Willian"

# OBS: Em outras linguagens de programação: qualquer caracter, nomes, textos, podem ser declarados como (char =)
# EXEMPLO ABAIXO:

char = "j"
char = "o"
char = "w"
char = "i"

nome3 = '''ASPAS TRIPLAS SIMPLES: É um exemplo de string longa, contendo
algumas informações.'''

nome4 = """ASPAS TRIPLAS DUPLAS: É um exemplo de string longa, contendo
algumas informações."""

# OBS: Todo print: É uma função para mostrar, ou seja, o usuário ler na tela o que será
# impresso a ele.

print(nome)
print(nome2)
print(nome3)
print(nome4)

# LAÇO DE REPETIÇÃO (For) = PARA.

# Enquanto esse laço de repetição ocorrer entre o parâmetro colocado entre aspas "" essa palavra irá se completar.
# Então a palavra irá ser concluída de acordo com o que colocarmos entre os parênteses.

for i in "Python":
   print(i)


# Esse outro exemplo, funciona da mesma forma, só que aqui, criamos uma variável, atribuímos os valores e assim utilizamos o parâmetro de
# acordo com os dados acrescentados. Utilizamos o Laço (for) para criar o mesmo. E o print para imprimir os dados atribuidos.

num = [4, 5, 6, 7, 8, 9, 10]

for j in num:
    print(j)

# Laço for Range = Uma série de valores atribuídos, ou podemos dizer que também seja um alcance até determinado limite!

for i in range(10):
    print(i + 1)

# Nesse laço, criamos uma sequência, nesse caso o alcance será até o limite atribuído 10.
# Como vemos foi adicionado + 1, de acordo os dados passados.
# Assim podemos utilizar esse laço para percorrer uma lista e diferentes dados.

print("==========")

# Nesse caso, estamos criando um  parâmetro para iniciar de -10 até 0, assim de 1 em 1.
for j in range(- 10, 0, 1):
    print(j)

    # Quando printarmos a contagem será dada de 1 em 1.
    # Se colocarmos agora 2 no terceiro parâmetro, ele irá pular de 2 em 2.

for j in range(- 10, 0, 2):
    print(j)


# Laço de Repetição (While) = ENQUANTO.
# criando uma variável, contado, por exemplo podemos colocar qualquer letra, nesse exemplo vamos utilizar a letra (i).

# while = Enquanto

# Aqui atribuo que (i), é igual a 0, enquanto (i) for menor ou = 10, o contador irá adicionando + 1 a sua contagem.

# Então, acontece que  o (i) chegando no numeral 10 ele para de adicionar + 1, assim se encerra no 10.

i = 0

while (i <= 10):
    print(i)
    i = i + 1


# MANIPULAÇÃO DE DADOS

# print, comando para mostrar conteúdo na tela do usuário, função para saída de dados.
print("Olá mundo!")

nome = "Willian"
idade = 27
peso = 110.0
altura = 1, 87

print(nome)
print(idade)
print(peso)
print(altura)

print("Meu nome é: ", nome, ",minha idade é: ", idade,",atualmente peso: ", peso, "e a altura: ", altura)

# Função sep='/', ele faz a separação de forma automática diante os números.
# print("20", "11", "1995", sep='/')

# EXISTE TAMBÉM O SEPARADOR COM TRACINHO, DE VEZ DE COLOCAR A BARRA, SE COLOCA O TRAÇO!

print("20", "11", "1995", sep='/')
print("B", "n", "n", ".", sep="a")

# ACRESCENTANDO ESPAÇO, ACRESCENTANDO END= " "

print("Vamos estudar na", end=" ")
print("SoulCode Academy.")

print("Preço ", end="R$ ")
print(50.0)

# COMANDO ELIF
numero = 13
# O comando elif = então, você acrescenta condições, sugestivas, caso o número for de acordo com as condições estabelecidas a seguir,
# o resultado sairá de acordo com as opções de elif, ou seja, então!

if numero == 10:  # True, Se
    print("Este número é igual a 10!")
elif numero == 11:
    print("Este número é igual a 11!")
elif numero == 12:
    print("Este número é igual a 12")
elif numero == 13:
    print("Este número é igual a 13")
else:  # False, Senão
    print("Este número não é igual a 10, a 11, a 12 ou 13!")
