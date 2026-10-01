import datetime #importando módulo para pegar o ano

numero_atendimento = int(input("Digite o número do atendimento: "))#solicitando o número do atendimento
nome = input("Digite seu nome completo: ").title().split()#solicitando nome e tartando a string
ano = datetime.datetime.now().year#pegando o ano 

iniciais = ''.join([cname[0] for cname in nome])

print("-"*20)
print(f"Protocolo {ano}-{numero_atendimento:0>4}-{iniciais}")
print("-"*20)
input('Aperte enter para finalizar...')

'''
Na aula 08, são mostrados os módulos, que são basicamente agrupamentos de funções que têm objetivos em comum. Por exemplo, o módulo `math`, que tem como objetivo fornecer funções matemáticas (`sqrt`, `sin`, `cos`, ...). Porém, essas funções não podem ser usadas automaticamente no código; antes, é necessário importá-las. Para importar o módulo, é preciso escrever `import nome_do_módulo`. Mas, se eu quiser importar apenas uma função específica do módulo, basta digitar `from nome_do_módulo import nome_da_função`.

Exemplos:
import math
from math import sqrt

Caso eu importe o módulo para utilizar uma função, tenho que digitar `nome_do_módulo.nome_da_função`. Caso eu importe apenas a função do módulo, basta escrever o nome da função.

Exemplos:
import math
math.sqrt(4) == 2

```
from math import sqrt
    sqrt(4) == 2
```

Outra biblioteca citada no vídeo é a `random`, que possibilita aleatorizar dados.

Exemplos:
import random
random.random() => me retorna um número aleatório entre 0 e 1.
random.randint(x, y) => me retorna um número aleatório entre x e y.

Além disso, é possível importar outros módulos que não sejam nativos da linguagem.
'''
#--------------------------------------------------------------------------------------#
'''
No vídeo 9, é mostrada a manipulação de strings, já que uma string não passa de uma sequência de caracteres, sendo possível realizar diversas manipulações na mesma.

Primeiro, é mostrado como pegar um caractere específico da string. Basta digitar o nome da variável entre colchetes e colocar a posição dela na string. Lembrando que a primeira posição é a posição 0 e que os espaços também contam como posição.

Exemplo:
texto = 'Ola mundo'
# Para pegar a letra m, basta colocar:
texto[4]

Mas, para pegar uma sequência de caracteres, basta escrever:

Exemplo:
texto = 'Ola mundo'
texto[0:2]
# Ele vai pegar "Ol", já que o primeiro valor dos colchetes indica de onde eu quero pegar o primeiro caractere, e o segundo valor indica até onde quero pegar a string.

Além disso, existe um terceiro valor que indica de quanto em quanto eu quero pegar os caracteres da string.

Exemplo:
texto = 'Ola mundo'
texto[0:10:2]
# Nesse caso, ele vai pegar os caracteres de 2 em 2. Ou seja, o retorno vai ser:
oamno

Se eu ocultar o primeiro valor, ele vai pegar do começo até o valor que antecede o segundo. Se eu ocultar o segundo, ele vai pegar do primeiro valor até o último.

Exemplo:
texto = 'Ola mundo'
texto[:3] # Retorna Ola
texto[4:] # Retorna mundo

Além disso, existem funções para analisar ou modificar strings. Por exemplo, a função `len` verifica o tamanho da string; a função `count` retorna quantas vezes determinado caractere aparece; a função `find` retorna a posição em que determinada sequência de caracteres foi encontrada na string; a palavra reservada `in` verifica se determinada coisa está presente na string; o `replace` substitui uma palavra por outra.

Também existem funções que mudam a formatação da string. O `upper` deixa toda a string em caixa alta; o `lower` deixa toda a string em caixa baixa; o `capitalize` deixa a primeira posição da string maiúscula e as demais minúsculas; o `title` deixa o começo de todas as palavras da string em maiúsculo e as demais letras em minúsculo; o `strip` tira os espaços do começo e do final da string; o `split` separa a string nos espaços entre as palavras, fazendo com que cada palavra vire um item de uma lista; e o `join` une as strings separadas em uma só.

Exemplos:
texto = 'Hyan é fera'
len(texto) => 11

```
texto.count('a') => 2
# No count, eu também posso aumentar o ponto inicial da verificação.
texto.count('a', 3) => 1

texto.find('Hyan') => 0
# Se a sequência não aparecer na string, ele retorna -1.

'fera' in texto => True

texto.replace('Hyan', 'Gabriel') => Gabriel é fera 

texto.upper() => HYAN É FERA
texto.lower() => hyan é fera
texto.capitalize() => Hyan é fera
texto.title() => Hyan É Fera

texto2 = '   Mariana e Augusto são legais   '
texto2.strip() => 'Mariana e Augusto são legais'
# Também posso retirar apenas da direita ou somente da esquerda.
texto2.lstrip() => 'Mariana e Augusto são legais   '
texto2.rstrip() => '   Mariana e Augusto são legais'

palavras = texto2.split() => ['Mariana', 'e', 'Augusto', 'são', 'legais']

' '.join(palavras) => 'Mariana e Augusto são legais'

'''
