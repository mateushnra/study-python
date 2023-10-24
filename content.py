# Não é necessário declarar
# Tipagem dinâmica (muda de tipo apenas atribuindo o conteúdo respectivo ao tipo)
var = 3 #int
var = 3.14 #float
var = "Texto" #str
var = True #bool
var = [1, 2, 3] #list
var = {'name': "Mateus", 'age': 100} #dict
var = ('a', 'b', 'c') #tuple
var = 2+3j #complex
var = range(0,6,2) #range
var = {"a", "b", "c"} #set 
var = frozenset({"a", "b", "c"}) #frozenset
var = bytearray(5) #bytearray
var = memoryview(bytes(5)) #memoryview
var = None #NoneType

# As variáveis são objetos, portanto possuirão métodos de acordo com o tipo para poderem ser manipuladas
a = int(13) # Utilizando o construtor para dar um valor para a

# Para pegar o tipo da varíavel use o comando
type(var)

# Para exibir algo no console utilize o comando print()
print("Hello World!")
print("Hello" + " World!") #Concatenando dentro do print()

# O que é falso para o Python
falso = bool('') #String vazia retorna falso
falso = bool(0) #Valor ZERO retorna falso
falso = bool(()) #Tupla vazia retorna falso
falso = bool([]) #Lista vazia retorna falso
falso = bool({}) #Dicionário vazio retorna falso

# Atribuição Múltipla
nome = "Henrique"
sobrenome = " Mateus"

# Atribui simultaneamente valores para duas variáveis
nome, sobrenome = sobrenome, nome 
x, y = 1, 4

# Apenas existe o tipo str
string = 'texto' #Funciona com aspas simples
string = "texto" #Funciona com aspas duplas

# Comando Ord() recebe o valor numérico correspondente a tabela ASCII de um caracter
ord("A") #Retorna o valor númerico de ASCII de 'A'
ord('AB') #Da erro, pois retorna caso haja apenas 1 caracter

# Comando chr() retorna o caracter correspondente ao valor númerico da tabela ASCII
ord(65) #Retorna o caracter respectivo ao valor 65 que é "A"

# Operadores Aritméticos
1 + 1 #Soma
1 - 1 #Subtração
1 * 1 #Multiplicação
1 / 1 #Divisão
5 / 2 #Retorna 2, em vez de 2.5
5 / 2. #Retorna 2.5
10 % 2 #Módulo
2 ** 4 #Potência

# Operadores de atribuição
a += 3 #a = a + 3
a -= 3 #a = a - 3
a *= 3 #a = a * 3
a /= 3 #a = a / 3
a %= 3 #a = a % 3
a //= 3 #a = a // 3 (divisao arredondando para baixo)
a **= 3 #a = a ** 3

# Operadores de comparação
2 > 1 #Maior 
2 >= 1 #Maior igual
1 < 2 #Menor
1 <= 2 #Menor igual
3 == 3 #Igualdade
3 != 2 #Diferente

3 < 10 < 20 #Funciona comparação com mais de 2 valores simultaneamente, mas caso um retorne falso, será falso o retorno total do comando

# Operadores lógicos
3 > 5 and 3 > 1 #operador AND
3 > 5 or 3 < 5 #Operador OR
not 0 #Inverte o valor lógico (True ou False) que a condição retorna

#Retornando valores especificos de uma String
texto = "Teste de escrita"
texto[0] #Retorna o primeiro caracter da String, correspondente ao indíce 0, nesse caso 'T'
texto[:10] #Retorna do início da string até mais 10 indíces ou seja, do 0 ao 9
texto[3:] #Retorna a partir do indice 3 até o fim da String
texto[3:10] #Retorna a partir do indice 3 até mais um antes do indice 10 da String
texto[2::2] #Retorna a partir do indice 2 e pega todos os valores em um intervalo de 2 indices, ou seja os indices recebidos seriam 2, 4, 6, 8, 10... até o último possível dentro do vetor de str
texto[-1] #Retorna o último indice da String, e assim por diante, caso fosse -2, seria o penultimo.
texto[:-3] #Retorna do início da String até um valor antes do -3, que seria o -4.
texto[-10:9] #Retorna a partir do indice -10, até o indice 8
texto[::-1] #Retorna a String invertida, pois retorna do Fim da String, com o intervalo de -1, ou seja vai indo fim ao inicio

# Concatenação de Strings
nome = "Mateus"
sobrenome = "Henrique"
Completo = nome + ' ' + sobrenome 

# Operador de formatação de string %
nome = "Mateus" #%s formata strings
idade = 20 #%d formata numeros inteiros
valor_decimal = 3.14 #%f formata numeros flutuantes
valor_hexadecimal = 255 #%x formata numeros em hexadecimal
char = 'A' #%c formata strings com apenas 1 caracter

info = "Nome: %s \nIdade: %d \nValor Decimal: %f \nValor Hexadecimal: %x \nCaracter: %c" %(nome, idade, valor_decimal, valor_hexadecimal, char)

# Formatando String com .format
nome = "Mateus"
idade = 20

info = "Nome: {} \nIdade: {}" #{} representa que um valor que será passado no format entrará ali
info = info.format(nome, idade) #O valor passado substituirá {} na ordem respectiva passada

info = "Nome: {} \nIdade: {}".format(nome, idade) #Também funciona diretamente dessa forma

# Operador de multiplicação em uma String
texto = "-" * 5 #Repete o - 5 vezes, ou seja concatena 5 vezes a mesma coisa

# Ignorando o \ como caracter especial em uma string
c = "c:\dir\teste" #Não irá exibir o caracter \
c = "c:\\dir\\teste" #Repetindo \\ duas vezes resolve
c = r"c:\dir\teste" #Inserindo um r antes da string também indica que não serão interpretados quaisquer caracter especiais

# Para respeitar a quebra de linha dentro da própria string é possivél criar uma string com 3 aspas duplas
poesia = """Eu cavo,
Tu cavas,
Ele cava,
Não é bonito,
Mas é profundo..."""

poesia = '''Eu cavo,
Tu cavas,
Ele cava,
Não é bonito,
Mas é profundo...''' #Também funciona com aspas simples

# Tipo Unicode (usado para representar textos de qualquer sistema de escrita)
texto = u"Texto em Unicode" #O u no início transforma o str em unicode
type(texto) #Retorna unicode

# Para descobrir os métodos de um objeto usa-se o comando dir()
dir(str) #Retorna os métodos de um objeto do tipo string

# Métodos para o tipo string
texto.capitalize() #Retorna a string com a primeira letra em maiúsculo e diminui todas as outras letras para minúsculo
texto.center(20) #Centraliza a string distribuindo métade do valor para cada lado, e descontando o tamanho da string, ou seja, caso a string tenha 20 caracteres, nao acontecera nada, mas caso tenha 18, será um espaço para esquerda e 1 para a direita
texto.split('-') #divide a string em uma lista, cortando o caracter procurado e separando o que vem antes e depois dele, caso não tenha nada antes e depois dele, será cortado como uma string vazia ''
texto.upper() #Transforma tudo em maiúsculo
texto.lower() #Transforma tudo em minúsculo
texto.strip() #Remove qualquer espaço em branco antes da string começar e depois de terminar
texto.replace("M", "A") #Troca tudo que for da esquerda pelo da direita
len(texto) #Retorna quantos caracteres tem uma string
max(texto) #Retorna o maior item de uma sequência, no caso o maior valor de caracter convertido em valor numérico da tabela ASCII
min(texto) #Retorna o menor item de uma sequência, no caso o menor valor de caracter convertido em valor numérico da tabela ASCII

# Retornando o valor absoluto de um número
abs(-69) #Retorna 69 que é o valor absoluto

# Retornando o menor e maior valor numérico
max([3,5]) #Caso a variavel ou o dado analisa pelo max() receba um tipo de dado que receba mais de 1 valor numérico, ele retorna o maior
min([1,5]) #Retorna o menor valor numérico

# Potência com 2 parametros
pow(2, 4) #Mesmo que 2 ** 4

# Potência com 3 parametros
pow(4, 3, 5) #Retorna o módulo da potência, ou seja, no caso seria (4 * 4 * 4) % 2 = 0

# Conversão de tipos entre variaveis
a = str(3)
a = int("3")
a = float("3.14")

# Inserindo caracteres conflituosos ou ilegais em uma string ("", \\, \n, \t, \b,)
texto = "We are the so-called "Vikings" from the north." #Vai dar erro, para colocar entre "" utilize o \\ 
texto = "We are the so-called \"Vikings\" from the north." #Exibe "Vikings" 
texto = "We are the so-called \\Vikings\\ from the north." #Exibe \Vikings\
texto = "We are the so-called \nVikings\n from the north." #Quebra a linha entre os textos antes e depois do \n
texto = "We are the so-called \tVikings\t from the north." #Exibe "We are the so-called    Vikings  from the north.", ou seja há um tab de distância onde havia \t
texto = "We are the so-called \bVikings\b from the north." #Apaga o caracter anterior, ficando "We are the so-calledViking from the north."




