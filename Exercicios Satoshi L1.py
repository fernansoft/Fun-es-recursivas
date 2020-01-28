#Exec01 - Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.
lado = float(input('Insira o lado do quadrado: '))
area = lado * lado
print('O valor da área é: ', area)

#Exec02 - Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.
salario = float(input('Insira o salário atual: '))
novosalario = salario * 1.15
print('O novo salário será de: ', novosalario)

#Exec03 - Receba a base e a altura de um triângulo. Calcule e mostre a sua área.
base = float(input('Insira o valor da base do triângulo: '))
altura = float(input('Insira o valor da altura do triângulo: '))
area = (base * altura) / 2
print('A área do triângulo é: ', area)

#Exec04 - Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = ((9*C+160) /5).
celsius = float(input('Insira a temperatura em Celsius (C°): '))
fahrenheit = (9 * celsius + 160) / 5
print('A temperatura equivalente em Fahrenheit é: ', fahrenheit)

#Exec05 - Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes).
a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))
delta = ((b ** 2) - (4*a*c))
x1 = (((-b) + (delta ** (1/2)))/(2 * a))
x2 = (((-b) - (delta ** (1/2)))/(2 * a))
print('As raízes da equação são:\n X1: {}\n X2: {}'.format(x1, x2))

#Exec06 - Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.
x = float(input('Insira x: '))
y = float(input('Insira y: '))
aux = x + y
x = aux - x
y = aux - y
print('O novos valores são:\n X: {}\n Y: {}'.format(x, y))

#Exec07 - Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.
comprimento = float(input('Insira o comprimento: '))
largura = float(input('Insira a largura: '))
altura = float(input('Insira a altura: '))
volume = comprimento * largura * altura
print('O volume do paralelepípedo é de {} m³'.format(volume))

#Exec08 - Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.
deposito = float(input('Insira o valor a ser depositado: '))
print('O valor a ser resgatado é de: R${:.2f}\nTendo R${:.2f} de rendimento!'.format(deposito * 1.0013, deposito * 0.0013))

#Exec09 - Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
print('O resultado é {}'.format(((n1 ** 2) + (n2 ** 2))))

#Exec10 - Receba 2 números reais. Calcule e mostre a diferença desses valores.
n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
print('A diferença é: {}'.format(n1 - n2))

#Exec11 - Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência.
raio = float(input('Insira o valor do raio em cm: '))
print('O perímetro da circunferência é de:\n{:.3f}cm ou {:.3f}m'.format(2*3.14*raio, (2*3.14*raio)/100))

#Exec12 - Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.
anonasc = int(input('Insira o seu ano de nascimento: '))
anoatual = int(input('Insira o ano atual: '))
print('Você tem {} anos\nVocê terá {} anos daqui à 17 anos.'.format(anoatual - anonasc, anoatual + 17 - anonasc))

#Exec13 - Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
alimento = float(input('Insira a quantidade de alimento (em Kg): '))
print('Seu alimento irá durar {} dias, considerando que você come 50g por dia!'.format((alimento*1000)/(50)))

#Exec14 - Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.
ang1 = int(input('Insira o primeiro ângulo:'))
ang2 = int(input('Insira o segundo ângulo:'))
print('O valor do terceiro ângulo é {}!'.format(180 - ang1 - ang2))

#Exec15 - Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.
cateto1 = float(input('Insira o valor do primeiro cateto: '))
cateto2 = float(input('Insira o valor do segundo cateto: '))
hipotenusa = (((cateto1 ** 2) + (cateto2 ** 2))**(1/2))
print('Considererando os catetos {} e {}, a hipotenusa vale: {}'.format(cateto1, cateto2, hipotenusa))

#Exec16 - Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes. Calcule o salário, que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.
hrtrab = float(input('Insira a quantidade de horas trabalhadas (em decimal): '))
valhr = float(input('Insira o valor por hora: '))
desconto = float(input('Insira o percentual de desconto: '))
desconto = 1 - (desconto/100)
dependentes = float(input('Insira a quantidade de dependentes (caso houver): '))
salario = hrtrab * valhr
salliq = (salario * desconto) + (100 * dependentes)
print('O salario líquido será de R${:.2f}'.format(salliq))

#Exec17 - Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média. 
tpercurso = float(input('Insira o tempo do percurso em decimal: '))
velmedia = float(input('Insira a velocidade média estimada (em Km): '))
print('A quantidade de litros gastos é de {} litros'.format((tpercurso*velmedia)/12))

#Exec18 - Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor.
valor1 = int(input('Insira o primeiro valor inteiro: '))
valor2 = int(input('Insira o segundo valor inteiro: '))
if valor1 > valor2:
    print('A diferença do maior valor pelo menor é de: {}'.format(valor1 - valor2))
else:
    print('A diferença do maior valor pelo menor é de: {}'.format(valor2 - valor1))

#19. Receba 2 valores reais. Calcule e mostre o maior deles.
real1 = float(input('Insira o primeiro valor: '))
real2 = float(input('Insira o segundo valor: '))
if real1 > real2:
    print('O maior é o primeiro input, com valor de {}'.format(real1))
else:
    print('O maior é o segundo input, com valor de {}'.format(real2))

# 20. Receba 3 coeficientes A, B, e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))
x1 = 0
x2 = 0
delta = ((b**2)-4*a*c)
if delta < 0:
    print('Valor de delta negativo, não existe raizes reais para esta equação!')
else:
    x1 = (-b + (delta**(1/2)))/2*a
    x2 = (-b - (delta**(1/2)))/2*a
    if delta == 0:
        print('Valor de delta igual a zero, existe apenas uma raiz real para esta equação!\nSendo este: X = {}'.format(x1))
    else:
        print('Valor de delta maior que zero, existe duas raizes reais para esta equação!\nSendo estas: X1 = {}\nX2 = {}'.format(x1, x2))

# 21. Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média: 
# a. Se a média for >= 6,0 exibir “APROVADO”;
# b. Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
# c. Se a média for < 3,0 exibir “RETIDO”.
notasbimestrais = []
somanotas = 0
for i in range(4):
    nota = float(input('Insira a sua nota do {}° bimestre: '.format(i + 1)))
    while nota < 0 or nota > 10:
        print('As notas são valores que vão de 0 à 10!')
        nota = float(input('Insira a sua nota do {}° bimestre: '.format(i + 1)))
    notasbimestrais.append(nota)
for i in range(4):
    somanotas += notasbimestrais[i]
somanotas /= 4
if somanotas >= 6:
    print('APROVADO')
elif somanotas >= 3:
    print('EXAME')
else:
    print('RETIDO')

# 22. Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
val1 = int(input('Insira o primeiro valor inteiro: '))
val2 = int(input('Insira o segundo valor inteiro: '))
if val1 > val2:
    print('Os valores em ordem crescente é:\n1° Valor = {}\n2° Valor = {}'.format(val2, val1))
else:
    print('Os valores em ordem crescente é:\n1° Valor = {}\n2° Valor = {}'.format(val1, val2))


# 23. Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
encontre = 0
achei = 0
valores = []
valores.append(float(input('Insira o 1° valor: ')))
for i in range(2):
    valor = float(input('Insira o {}° valor: '.format(i + 2)))
    while valor < valores[i]:
        print('Será aceito apenas valores inseridos em ordem crescente')
        valor = float(input('Insira o {}° valor: '.format(i + 2)))
    valores.append(valor)
valores.append(float(input('Insira um 4° valor qualquer (não precisa ser crescente): ')))
print('Os valores apresentados em ordem crescente são:')
for i in range(4):
    while 
    for j in range(4):
        if encontre == valores[i]:
            print('{}° valor = {}'.format(i + 1, valores[i]))
    encontre += 1

#da tabuada
num = int(input('Insira o número: '))
print('A tabuada do número {} é:\n{} * 1 = {}\n{} * 2 = {}\n{} * 3 = {}\n{} * 4 = {}\n{} * 5 = {}\n{} * 6 = {}\n{} * 7 = {}\n{} * 8 = {}\n{} * 9 = {}\n{} * 10 = {}'.format(num, num, num * 1, num, num * 2, num, num * 3, num, num * 4, num, num * 5, num, num * 6, num, num * 7, num, num * 8, num, num * 9, num, num * 10))