#Exemplo
num = int(input('insira um número positivo desejado:'))
def ffat(n):
  if (n==1):
    return n
  else:
    f = (n * ffat(n-1))
  return f
print ('valor fatorial', ffat(num))

#serie01
num = int(input('insira um número positivo:'))
while num < 0:
  print('insira apenas valores positivos!')
  num = int(input('insira um número positivo'))
def fs01(n):
  if (n >= 100):
    return n
  else:
    s = (n + fs01(n + 1))
    return s
print('A soma dos valores até 100 é:', fs01(num))

#serie02
num = int(input('insira o enésimo número: '))
def fs02(n):
  if (n < 1):
    return n
  else:
    s = (n + fs02(n - 1))
    return s
print('O resultado é:', fs02(num))

#serie03
num = float(input('digite o enésimo número: '))
def fs03(n):
  if (n <= 1):
    return n
  else:
    s = ((n ** (-1)) + fs03((n-1) ** -1))
    return s
print('o resultado é: ', fs03(num))
#naodeucerto aaaaa

#serie04
num = float(input('insira o enésimo número: '))
denominador = 1
def fs04(n):
  if (n < 1):
    return n
  else:
    s = ((n/denominador) + fs04((n - 1)/(denominador + 1)))
    return s
print('o resultado é: ', fs04(num))
