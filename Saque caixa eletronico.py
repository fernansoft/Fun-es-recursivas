#SAQUE
n50 = int(0)
n20 = int(0)
n10 = int(0)
n05 = int(0)
n02 = int(0)
saque = int(input('insira o valor a ser sacado:'))
while saque > 53 or saque == 50:
    saque = saque - 50
    n50 = n50 + 1
while saque > 23 or saque == 20:
    saque = saque - 20
    n20 = n20 + 1
while saque > 13 or saque == 10:
    saque = saque - 10
    n10 = n10 + 1
if saque == 11 or saque == 13:
    saque = saque - 5
    n05 = n05 + 1
if saque == 6 or saque == 8:
    while saque >= 2:
        saque = saque - 2
        n02 = n02 + 1
else:
    while saque >= 5:
        saque = saque - 5
        n05 = n05 + 1
    while saque >= 2:
        saque = saque - 2
        n02 = n02 + 1
print('as notas a serem sacadas são:\n {} notas de R$50,00\n {} notas de R$20,00\n {} notas de R$10,00\n {} notas de R$05,00\n {} notas de R$02,00'.format(n50, n20, n10, n05, n02))
