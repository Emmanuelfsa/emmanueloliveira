salário = float(input('Qual o salário do Funcionário? R$'))
aumento = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, aumento))
