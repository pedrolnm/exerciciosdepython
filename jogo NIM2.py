def computador_escolhe_jogada(n, m): 

    if n <= m:
        jogada = n
    elif n % (m + 1) != 0:
        jogada = n % (m + 1)
    else:
        jogada = m
    return jogada

    

def usuario_escolhe_jogada(n, m):
    jogada = int(input('quantas peças você vai tirar? '))
    print()
    while jogada > m or jogada <= 0 or jogada > n:
        print('Oops! Jogada inválida! Tente de novo. ')
        print()
        jogada = int(input('quantas peças você vai tirar? '))
        print()
    return jogada
        
def campeonato():
    pontosUsuario = 0
    pontosComputador = 0
    c = 1
    while c <= 3:
        print()
        print(f'**** Rodada {c} ****')
        print()
        resultado = partida() 
        if resultado == 2:
            pontosUsuario += 1
        else:
            pontosComputador += 1
        c +=1
    print()
    print('**** Final do campeonato! ****')
    print()
    print(f'Placar: Você {pontosUsuario} X {pontosComputador} Computador')

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()
    if n % (m + 1) == 0:
        print('Você começa!')
        print()
        while n:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            if jogada == 1:
                print('Você tirou uma peça.')
            else:
                print(f'Você tirou {jogada} peças.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
                print()
            else:
                print('Agora resta apenas uma peça no tabuleiro.')
                print()
            if n == 0:      
                print('Fim do jogo! O usuário ganhou!')
                return 2
            jogada = computador_escolhe_jogada(n, m)
            if jogada == 1:
                print('O computador tirou uma peça')
            else:
                print(f'O computador tirou {jogada} peças')
            n -= jogada
            if n > 0:
                print(f'Agora restam {n} peças no tabuleiro!')
                print()
            if n == 0:      
                print('Fim do jogo! O computador ganhou!')
                return 1
    else:
        print('Computador começa!')
        print()
        while n:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            if jogada == 1:
                print('O computador tirou uma peça')
            else:
                print(f'O computador tirou {jogada} peças')
            if n > 0:
                print(f'Agora restam {n} peças no tabuleiro!')
                print()
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                return 1
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            if jogada == 1:
                print('Você tirou uma peça.')
            else:
                print(f'Você tirou {jogada} peças.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
                print()
            else:
                print('Agora resta apenas uma peça no tabuleiro.')
                print()
            if n == 0:
                print('Fim do jogo! O usuário ganhou!')
                return 2



print('Bem-vindo ao jogo NIM! Escolha:')
print()
print('1 - para jogar uma partida isolada')
part = int(input('2 - para jogar um campeonato '))
print()
while part != 1 and part != 2:
    print('Opção inválida, tente de novo! ')
    print('1 - para jogar uma partida isolada')
    part = int(input('2 - para jogar um campeonato '))  

if part == 1:
    print('Você escolheu uma partida isolada!')
    partida()
else:
    print('Você escolheu um campeonato!')
    campeonato()
    

        



