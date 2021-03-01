from random import randint
computador = randint(0, 5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print('-=-' * 20)
jogador = int(input(' Em que núemro pensei? ')) # Jogador tenta advinhar
if jogador == computador:
    print('Você venceu')
else:
    print('Você perdeu4')