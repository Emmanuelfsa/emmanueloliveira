nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando entre {:.1f} e {:.1f} a média é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('O aluno está REPROVADO!')
elif media >=5 and media < 7:
    print('O aluno está em RECUPERAÇÃO!')
elif media >= 7:
    print('O aluno está APROVADO!')