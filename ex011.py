Larg = float(input('Largura da parede: '))
Alt = float(input('Altura da parede: '))
área = Larg * Alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(Larg, Alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
