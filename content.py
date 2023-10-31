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
var = lambda a : a + 10 #Function
var = b"Texto" #bytes
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

# Operadores de identidade
x = [3, 4, 5]
y = [3, 4, 5]
z = x
#Esses operadores funcionam apenas comparando objetos, ou seja, tuplas, listas, dicionarios, etc...
x is y #Retorna false, pois x não é o mesmo objeto com a mesma memória, tendo apenas valores iguais
x is z #Retorna true, pois z recebeu x, portanto possui a mesma memória
x is not y #Retorna true, sendo a negação do is

# Operadores de pertencimento
x = ["apple", "banana"]
"banana" in x #Retorna true, pois existe o valor "banana" dentro de x
"apple" not in x #Retorna false, pois existe o valor "apple" dentro de x, sendo o not in a negação de in

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

#In e not in em strings
x = "apple"
"pl" in x #Retorna true, pois existe a sequencia "pl" dentro daquela string
"pl" not in x #Retorna false

# Retornando o valor absoluto de um número
abs(-69) #Retorna 69 que é o valor absoluto

# Retornando o menor e maior valor numérico
max([3,5]) #Caso a variavel ou o dado analisa pelo max() receba um tipo de dado que receba mais de 1 valor numérico, ele retorna o maior
min([1,5]) #Retorna o menor valor numérico

# Potência com 2 parametros
pow(2, 4) #Mesmo que 2 ** 4

# Potência com 3 parametros
pow(4, 3, 5) #Retorna o módulo da potência, ou seja, no caso seria (4 * 4 * 4) % 2 = 0

# Arredondando
round(3.2) #Arredonda para o inteiro mais próximo
round(3.13918934, 2) #Ao utilizar o segundo parâmetro do round(), ele indica quantas casas após a virgula irão aparecer, assim sendo arredondado para o mais próximo, no caso do exemplo a saída é de 3.14
round(3.50) #Quando o numero sendo arredondado estiver no meio exato, ambos os lados estarão igualmente próximos, portanto o arredondamento será definido para o lado par, se arredondar para cima é um numero par, então será para cima, caso contrário para baixo
round(0.5) #0
round(1.5) #2
round(2.5) #2
round(3.5) #4

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

#If
a = 1
b = 2
if a < b:
   print(a)
#Versão curta do if acima ^, como não existe else é possível resumir da seguinte forma:
if a < b: print(a) 
else: print(b)

#If...Else
a = 1
b = 2
if a > b:
   print(a)
else:
   print(b)
#Versão curta do if...Else acima ^, como não existe else é possível resumir da seguinte forma:
if a > b: print(a) 
else: print(b)
#Versão mais curta ainda, ou conhecida como if ternário
print(a) if a > b else print(b) #É possível exibir diferentes coisas em cada situação em um if ternário
a = 3 if a > b else 5 #Ou apenas é possível tratar uma variável ou dado, no sentido em que, você define o que será atribuido, e o else é apenas o valor ou calculo que será atribuido caso não cumpra com a condição, portanto não tem como fazer com que por exemplo, b = 5, pois é a que está sendo tratado

#If...Else if
a = 1
b = 2
if a > b:
   print(a)
elif a < b:
   print(b)

#If...Else if...Else
a = 1
b = 2
c = 3
if a > b:
   print(a)
elif a < b:
   print(b)
else:
   print(c)
#Else if com Else ternário
print("A") if a > b else print("=") if a == b else print("B")

#While Loop
i = 1
while i < 6:
  print(i)
  i += 1
#Break
i = 1
while i < 6:
  print(i)
  break #Executa o que esta antes dele, mas caso seja executada essa linha o while é terminado
  i += 1
#Continue
while i < 6:
  print(i)
  continue #Executa o que estiver antes, mas ao executar essa linha para na hora e volta para o início do loop
  i += 1
#Else no while
while i < 6:
  print(i)
  i += 1
else: #Funciona de forma que assim que o while terminar de ser executado, ou seja a condição não for ainda True, ele executa o código abaixo
  print("Terminou")
#Utilizando break, continue e else simultaneamente
while i < 6:
  print(i)#Executa
  break#Encerra o while
  i += 1
  continue#Volta para o inicio do bloco
  i += 2
else: #Caso chegue no break dentro do bloco acima, o else não chega a ser executado, pois o laço foi interrompido e terminado
  print("Terminou")

# For Loop
inicio = 0
fim = 10
for x in range(inicio, fim):# O range define o inicio do looping e após a vírgula o fim, ou seja range(0, 5) percorre, executa 5 vezes o looping, incrementando automaticamente o valor inicial, em que será percorrido da seguinte forma: 0, 1, 2, 3, 4. Ou seja, inicia no valor de inicio e termina no valor do fim - 1. E o valor será atual será passado para a variável declarada automaticamente antes do in
   print(x)

intervalo = 2
for x in range(inicio, fim, intervalo):#Com 3 parâmetros o for irá percorrer do inicio ao fim, incrementando ou decrementando de acordo com o valor passado no intervalo, ou seja ficará: 0, 2, 4, 6, 8, 10
   print(x)

nome = "Mateus"
for x in nome:#Podemos passar uma variavel no for em vez de um range(), desde que seja uma coleção de dados como lista, tupla, set e dicionário ou uma string
   print(x)#Exibe letra por letra
   
for x in "Mateus":#Também é possível passar o valor direto
   print(x)

#Break no for
for x in nome:
   print(x)
   break#Encerra o for sem percorre até o fim

#Continue no for
for x in nome:
   print(x)
   continue#volta para o inicio do for sem executar o que estiver abaixo, mas continua seguindo e executando normalmente
   a = x + "a"

#Else no for
for x in nome:
   print(x)
else: 
   print(nome)

# Listas
lista = [3, "apple", 3.14, 3, True] #Declarada com [], é heterogenea, possui tipos diferentes no mesmo conjunto, pode ser alterada, permite valores duplicados, possui indices iniciando em [0] e são ordenadas (na ordem em que insere os valores é como ficam)

#Instanciando uma lista
minhaLista = list(("apple", "banana", "cherry")) #O construtor é list(), em que como parametros deve ser passado (..., ...) para criar os valores
minhaLista = list(["apple", "banana", "cherry"]) #Funciona tambem passando [..., ...]
minhaLista = list({"apple", "banana", "cherry"}) #Funciona tambem passando {..., ...}

#Acessando valores da lista
minhaLista[0] #Primeiro valor da lista
minhaLista[-1] #Ultimo valor da lista
minhaLista[2:5] #Assim como nas Strings, funciona os intervalos de valores para serem exibidos na lista

#Trocando valores da lista
minhaLista[0] = "Orange" #Substitui o que era o primeiro valor da lista, por "Orange", o indice deve existir dentro da lista para que o valor possa ser trocado, não sendo possível adicionar novos valores atribuindo algo a um indice depois do último valor
thislist = ["apple", "banana", "cherry", "orange"]
thislist[1:3] = ["blackcurrant", "watermelon"] #Troca "banana" e "cherry", pelos respectivos valores

#Adicionando valores na lista
thislist.insert(2,"kiwi") #Adiciona no indice [2], o valor "kiwi", ou seja o que estava antes no indice [2], será passado para o indice [3], e assim a lista terá um novo elemento
thislist.append("orange") #Adiciona o valor para o final da lista diretamente, sem necessidade de informar o indice

#Inserindo uma nova lista dentro de outra lista
lista1 = ["A", "B", "C"]
lista2 = [1, 2, 3]
lista1 = lista1 + lista2 #Adiciona a segunda lista no final
lista1.extend(lista2) #Adiciona no final da lista1 a lista2
#O extend também adiciona tuplas, dicionarios e sets no final de uma lista, enquanto a concatenação não funciona mais
lista1 = ["A", "B", "C"]
lista2 = (1, 2, 3)
lista1.extend(lista2)

#Removendo itens da lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #Retira "banana" da lista ficando apenas dois valores
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") #Caso tenha dois valores iguais, ele remove apenas o primeiro
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #Retira o valor "banana"
thislist.pop() #Retira o ultimo valor da lista
del thislist[2] #Remove o indice [2]
del thislist #Remove a lista
thislist.clear() #Limpa a lista, mas nao deleta ela, ou seja no final ficara thislist = []

#Usando loop em listas
thislist = ["apple", "banana", "cherry"]
#A lista abaixo será percorrida do inicio ao fim
for x in thislist: #x é a variavel que sera utilizada para receber o valor atual da lista thislist do loop
    print(x) #Vai exibir cada valor um por um da lista inteira

for indice, valor in enumerate(thislist): #indice é a variavel que receberá o indice atual no loop da lista, e o valor o valor atual
    print(indice + " -> " + valor)  #Exibe o indice e o valor correspondente, exemplo: 2 -> cherry

for i in range (len(thislist)): #Podemos percorrer a lista inteira usando o range também, e passando como valor final o tamanho da lista
    print(thislist[i]) #Agora não funciona direto o print(i), pois não é um for com in, é um for in range

#Percorrendo uma lista em um while
i = 0 #Iniciando o indice em 0
while i < len(thislist): #funciona de forma parecida com o for i in range(len(thislist))
  print(thislist[i])
  i += 1 #Como não é um for, devemos incrementar 1 manualmente

#Atalho para printar os valores de uma lista rapidamente
[print(x) for x in thislist]

#Descobrindo quantos do respectivo valor existe em uma lista
thislist = [2,1,3,4,1]
thislist.count(1) #Retorna 2, pois o valor 1 aparece duas vezes

#Retornando o indice de um elemento
thislist.index(1) #Retorna 1, pois o elemento 1 está na posição 1, sendo retornado apenas a primeira vez que o respectivo elemento aparece em caso de valores iguais

#Ordenando um lista em ordem alfabética
thislist = ["orange", "apple", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #Organiza a lista baseado na ordem alfabética, porém aceita apenas str como valores para que o sort() funcione
#Ordenando um lista númerica em ordem crescente
thislist = [1, 44, 3, 8, 2, 6]
thislist.sort()

#Ordenando em ordem decrescente listas de str ou numéricas
thislist.sort(reverse = True)
thislist.reverse()

#Copiando uma lista com o copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #mylist recebe os valores contidos em thislist, em vez de apontar para thislist

#Listas e dicionários pré-definidos são mutáveis
x = [1, 2, 3] #Definindo uma lista
y = x #y não está recebendo os valores de x, e sim esta apontando para o mesmo objeto de x
x.append(6) #Adiciona um novo valor a x
print(y) #Exibe [1,2,3,6], pois y aponta para x

x = [1, 2, 3] #Definindo os valores de x
y = x #y aponta para o x de cima
x = [1, 2, 3, 6] #Declarando de novo x e atribuindo outros valores
print(y) #Exibe [1,2,3], pois y esta apontando para o x de cima e não para a nova variável x declarada logo abaixo

# Tuplas
tupla = (3, "apple", 3.14, 3, True) #Declarada com (), é heterogenea, possui tipos diferentes no mesmo conjunto, NÃO pode ser alterada, permite valores duplicados e são ordenadas (na ordem em que insere os valores é como ficam)
tupla = ("apple") #É uma string
tupla = ("apple",) #Tupla com um valor apenas

#Instanciando uma tupla
minhaTupla = tuple(("apple", "banana", "cherry")) #O construtor é tuple(), em que como parametros deve ser passado (..., ...) para criar os valores

#Como tuplas não são mutáveis, caso queira alterá-las é preciso converter em uma lista e depois converter de volta em tupla
x = ("apple", "banana", "cherry")
y = list(x) #Criando uma nova variável para receber a tupla em forma de lista
y[1] = "kiwi" #Modificação qualquer
x = tuple(y) #Enviando de volta a lista em forma de tupla

#Enpacotando e Desempacotando valores de um tupla
minhaTupla = (3, "banana", 5) #Criar uma tupla trata-se de ato de "packing", ou seja enpacotar um tupla

(num1, fruta, num2) = minhaTupla #Você pode desempacotar valores de uma tupla em variáveis, ou seja na ordem respectiva da tupla as váriaveis irão receber os valores individuais
#São necessárias variáveis equivalentes a quantidade de valores para o desempacotamento
print(num1) #3
print(fruta) #"banana"
print(num2) #5

#Desenpacotando variáveis e listas de um tupla
minhaTupla = (3, "banana", "apple", 6)
(num1, *frutas, num2) = minhaTupla #Utilizar o asteristico em uma variável, indica que ela receberá uma lista, mesmo que de um valor, porém se a tupla possuir mais valores que váriaveis que receberão o desempacotamento, a variável do tipo list() receberá mais de um valor de acordo com a ordem e o que sobrar para ela
print(num1) #3
print(frutas) #["banana", "apple"]q
print(num2) #6

# Sets
set = {3, "apple", 3.14, 3, True} #Declarada com {}, é heterogeneo, possui tipos diferentes no mesmo conjunto, NÃO pode ser alterada (Ou seja os itens já presentes na criação são imutáveis, porém é possível adicionar novos e remover existentes), NÃO permite valores duplicados, NÃO possui indices e NÃO são ordenados (os valores aparecem em ordens diferentes a cada vez)

#Sets consideram o número 1 como True e o número 0 como False, portanto o primeiro a aparecer fica e o outro é tratado como duplicata
thisset = {"apple", "banana", "cherry", True, 1, 2}
thisset = {"apple", "banana", "cherry", 0, False, 2}

#Instanciando um set
thisset = set(("apple", "banana", "cherry")) #O construtor é set(), em que como parametros deve ser passado (..., ...) para criar os valores

#Acessando valores em um set
thisset = {"apple", "banana", "cherry"}
#Como não existe indices em um set, é necessário varrer ele com um for até encontrar o valor procurado
for x in thisset:
  print(x)

#Adicionando valores em um set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

#Adicionando um set dentro de outro set
thisset = {"apple", "banana", "cherry"}
otherset = {"pineapple", "mango", "papaya"}
thisset.update(otherset) #Receberá os 6 itens, os antigos mais os 3 novos do set otherset, porém quando exibir a ordem é aleatória

#Não precisa ser um set para adicionar dentro do set
thisset = {"apple", "banana", "cherry"}
lista = ["pineapple", "mango", "papaya"]
thisset.update(lista)

#Outro jeito de adicionar um set com outro é pelo union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #A diferença é que o union cria um novo set a partir da junção de dois, e não adiciona um novo set em um ja existente

#Removendo valores de um set
#Com remove da erro caso o valor passado não existir dentro do set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#Com discard mesmo o valor passado não existindo não da erro, e também não remove nada do set
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#Com pop() remove um item aleátorio
thisset = {"apple", "banana", "cherry"}
thisset.pop()

# Dicionarios
dicionario = {"cor": "azul", "fruta": "banana", "numero": 33} #Declarada com {}, é heterogêneo, possui tipos diferentes no mesmo conjunto, pode ser alterada, NÃO permite valores duplicados, são ordenados

#Instanciando um dicionario
thisdict = dict(name = "Mateus", idade = "20")#O construtor é dict(), em que como parametros deve ser passado (key: value, key: value) para criar os valores

#Acessando um dicionario
thisdict.get("name") #método get(), onde é passado a chave como parâmetro para receber o valor
thisdict["name"] #Assim como uma lista, usando as [] conseguimos indicar o indice e receber o valor
#Acessando as chaves
thisdict.keys() #Retorna as chaves do dicionário
#Acessando os valores
thisdict.values() #Retorna os valores apenas do dicionário
#Acessando usando o items()
thisdict.items() #Retorna uma lista com tuplas dentro, em que cada uma armazena dois valores (indice, valor), na ordem de cada item do dicionario

#Checando a existência de uma chave
"name" in thisdict #Retorna True, pois name é um indice presente no dicionario
"Mateus" in thisdict #Retorna False, pois "Mateus" é um valor dentro do dicionario e não um indice, mesmo existindo

#Alterando valores em um dicionario
thisdict["name"] = "John" #Altera o valor da chave name para o valor passado
thisdict.update({"name": "John"}) #Deve ser passado como parâmetro um dicionário, com a(s) chave(s) que deseja alterar, ou seja, da para mudar mais de um item simultaneamente

#Adicionando itens novos a um dicionário
thisdict["color"] = "blue" #Caso não haja o indice passado, ele será criado como um novo indice no final do dicionário, passando o valor depois do =
thisdict.update({"color": "blue"}) #Mesma coisa com o update ao passar um novo indice não existente no dicionário, é criado um novo valor no final do dicionário de acordo com a ordem criada

#Removendo itens de um dicionário
thisdict.pop("color") #Remove o item passado indicado pela chave, além disso ele retorna o valor tirado simultaneamente enquanto tira um item
thisdict.popitem() #Remove o último item do dicionário
del thisdict["color"] #Deleta o item assim como na lista e em outras coleções de dados
del thisdict #Deleta o dicionário
thisdict.clear() #Limpa o dicionário, deixando-o vazio

#Passando o dicionário por um looping 
for x in thisdict:
    print(x) #Printa os indices e não os valores

for x in thisdict:
    print(thisdict[x]) #Printa os valores baseado nos indices passados

for x, y in thisdict:
   print(x) #Printa os indices, mas não como são chamados, e sim o valor numérico, ou seja de 0 até tamanho - 1
   print(y) #Printa os indices do jeito que são chamados

for x in thisdict.values():
   print(x) #Printa os valores de cada indice, pois o for percorrerá uma lista retornada pelo comando thisdict.values() que apenas possui os valores

for x, y in thisdict.items():
   print(x) #Printa o indice
   print(y) #Printa o valor do indice   

#Copiando um dicionário
newdict = thisdict.copy() #Retorna o conteúdo inteiro do dicionário em vez de fazer a referencia a variavel thisdict
newdict = dict(thisdict) #Instancia um novo dicionário passando como parametros o dicionário que será copiado, assim evitando a referencia

#Aninhando dicionários
thisdict = {
   "dict1" : {
      "name": "Mateus",
      "idade": 20
   },

   "dict2" : {
      "name": "John",
      "idade": 20
   }
}
#Criando separado e passando a variavel

dict1 = {
  "name": "Mateus",
  "idade": 20
}

dict2 = {
  "name": "John",
  "idade": 20
}

thisdict = {
   "dict1": dict1,
   "dict2": dict2
}

#Acessando itens aninhado em um dicionário
thisdict["dict1"]["name"] #Retorna "Mateus"

#Funções em python

def minhaFuncao():
   print("Hello")

minhaFuncao() #Chamando a função

#Passando parâmetros
def minhaFuncao(name):
   print("Hello " + name)

minhaFuncao("Mateus")

#Definindo um valor padrão para um parâmetro
def minhaFuncao(name = "John"):
   print("Hello " + name)

minhaFuncao("Mateus") #Retorna "Hello Mateus"
minhaFuncao() #Retorna "Hello John"

#Definindo um valor padrão para um parâmetro
def minhaFuncao(nome, sobrenome):
   print("Hello " + nome + " " + sobrenome)

minhaFuncao("Mateus") #Da erro, pois passou-se apenas um valor para uma função que recebe 2 paraêmtros

#É possível passar vários dados ao mesmo tempo como forma de tupla em uma função
def minhaFuncao(*cores): #Só pode existir um parâmetro em uma função que recebe uma tupla dessa maneira
   print(cores)

minhaFuncao("azul", "vermelho", "roxo") #Os dados passados isoladamentes são armazenados na variável da função em forma de tupla

#É possível passar um os dados em forma de dicionário
def minhaFuncao(**cores):
   print(cores)

minhaFuncao(cor1 = "azul", cor2 = "vermelho", cor3 ="roxo") #Os dados passados isoladamentes são armazenados no dicionário, respectivamente chave e valor

#É possível passar os argumentos de forma que a ordem não importe, basta indicar ao passar os valores quais parâmetros estarão recebendo o respectivo valor
def minhaFuncao(cor1, cor2, cor3):
   print(cor1)

minhaLista(cor2 = "azul", cor3 = "vermelho", cor1 = "roxo")

#Retornando valores em uma função
def minhFuncao():
   return 5 * 2 #Retorna um valor numérico

minhaFuncao()

#A função retorna valores de tipos diferente sem necessidade de identificar o tipo, pois é dinâmica
def minhaFuncao():
   return "Hello World!"

minhaFuncao()

#Lambda Function
#A lambda funcion é uma versão rápida e simplificada de uma função, em que pode ter o tanto de parâmetros desejado e sempre retorna um valor
x = lambda a, b: a + b + 10 #Deve-se armazenar uma lambda function em uma variável

print(x(15, 5)) #Exibe o retorno da função lambda

#Usando funções com lambda functions
def minhaFuncao(n):
   return lambda a: a * n #É possível retornar uma lambda function dentro de uma função, assim o parametro que será passado dentro da função será o valor recebido como parâmetro da lambda function, portanto não é possível usar diretamente minhaFuncao(), antes deve ser criado uma variavel só para armazenar uma função lambda

duplicador = minhaFuncao(2) #duplicador irá ser uma variável do tipo function, que recebe a minhaFuncao() passando o valor 2 para o parâmetro da lambda function, portanto ao executar duplicador() será retornado o valor a partir da lambda
triplicador = minhaFuncao(3) #Como minhaFuncao() é uma função que retorna uma lambda é possível criar várias variáveis que recebem a lambda function diferente, sem ter q reescrevela, apenas mudando os argumentos que ela terá

print(duplicador(10))
print(triplicador(10))
