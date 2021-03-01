casa = float(input('Qual o valor da casa?R$'))
salário = float(input('Qual salário do comprador?R$'))
anos = int(input('Em quantos anos o comprador vai pagar a casa? '))
mínimo = salário * 30 / 100
prestação = casa / (anos * 12)
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO!')