#Exec01 - Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado
lado = float(input('Insira o lado do quadrado:'))
area = lado * lado
print('O valor da área é: ', area)

#Exec02 - Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%
salario = float(input('Insira o salário atual:'))
novosalario = salario * 1.15
print('O novo salário será de: ', novosalario)

#Exec03 - Receba a base e a altura de um triângulo. Calcule e mostre a sua área
base = float(input('Insira o valor da base do triângulo:'))
altura = float(input('Insira o valor da altura do triângulo:'))
area = (base * altura) / 2
print('A área do triângulo é: ', area)

#Exec04 - Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5
celsius = float(input('Insira a temperatura em Celsius (C°)'))
fahrenheit = (9 * celsius + 160) / 5
print('A temperatura equivalente em Fahrenheit é: ', fahrenheit)

#Exec05 - Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes)
a = float(input('Insira o valor de A:'))
b = float(input('Insira o valor de B:'))
c = float(input('Insira o valor de C:'))
delta = ((b ** 2) - (4*a*c))
x1 = (((-b) + (delta ** (1/2)))/(2 * a))
x2 = (((-b) - (delta ** (1/2)))/(2 * a))
print('As raízes da equação são:\n X1: {}\n X2: {}'.format(x1, x2))

#Exec06 - Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos
