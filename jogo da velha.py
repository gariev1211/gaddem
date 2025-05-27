matris =[['_','_','_'],
        ['_','_','_'],
        ['_','_','_']
]
for line in matris:
    for i in line:
        print(f'{i}', end=' ')
    print()

jogada_usuario1 = input('jogador1: ')
jogada_usuario2 = input('jogador2: ')
matris[jogada_usuario1[0],jogada_usuario1[1]] = 'X'
matris[jogada_usuario2[0],jogada_usuario2[1]] = 'O'
for linha in matris:
    for i in linha:
        print(f'{i}', end=' ')
    print()