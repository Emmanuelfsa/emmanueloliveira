distância = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
if distância <= 200:
    pago = distância * 0.50   
else:
    pago = distância * 0.45
print('O total da sua passagem é de tantos Reais R${:.2f}'.format(pago))   