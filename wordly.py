from funcoes_wordly import *
from palavras import lista_palavras
import random

#-----------------------------------------------------------começo do jogo -------------------------------------------------------------------------------------
print_slow('Bem vindo ao jogo:')
time.sleep(1.5)
print('''
    _   ___ _____   _____ _  _ _  _   _          _        ___  _   _      ___   _____    _   
   /_\ |   \_ _\ \ / /_ _| \| | || | /_\        /_\      | _ \/_\ | |    /_\ \ / / _ \  /_\  
  / _ \| |) | | \ V / | || .` | __ |/ _ \      / _ \     |  _/ _ \| |__ / _ \ V /|   / / _ \ 
 /_/ \_\___/___| \_/ |___|_|\_|_||_/_/ \_\    /_/ \_\    |_|/_/ \_\____/_/ \_\_/ |_|_\/_/ \_\ 
                                                                                             
''')
time.sleep(1.5)
tutorial_perg = input('\nVocê gostaria de um breve tutorial do jogo antes de começarmos? Digite "s" caso sim ou "n" caso não: ')
while tutorial_perg != 's' and tutorial_perg != 'n':
    tutorial_perg = input('\nVocê gostaria de um breve tutorial do jogo antes de começarmos? Digite "s" caso sim ou "n" caso não: ')

if tutorial_perg == 's':
    print_slow('\nNo jogo ADIVINHA A PALAVRA, você terá 6 tentativas para adivinhar uma palavra de 5 letras gerada aleatoriamente.')
    time.sleep(1)
    print_slow('\nPara te ajudar, existirão algumas dicas:')
    time.sleep(1)
    print_slow('\nO símbolo ⬜ significa que a letra não existe na palavra que você deve adivinhar;')
    time.sleep(0.7)
    print_slow('\nO símbolo 🟨 significa que a letra existe na palavra, mas não está na posição certa;')
    time.sleep(0.7)
    print_slow('\nO símbolo 🟩 significa que a letra existe na palavra e está na posição certa.')
    time.sleep(1)
    print_slow('\nEaí, está pronto para o desafio?')
    time.sleep(1)
    print()

começar_jogo = True
while começar_jogo:
    começar = input('\nPressione ENTER para começar o jogo: ')
    while começar != '':
        começar = input('Pressione ENTER para começar o jogo: ')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

    contador_tentativas = 6
    palavra_jogo = random.choice(lista_palavras)
    palavra_jogo = remove_acentos(palavra_jogo)
    palavra_jogo = palavra_jogo.lower()
    palavra_jogo = 'casei'

    while contador_tentativas  > 0:
        print_slow(f'Você possui {contador_tentativas} tentativa(s)!')
        palavra_tentativa = input('\nDigite uma palavra aleatória com 5 letras: ') #palpite do usuário
        while palavra_tentativa not in lista_palavras:
            palavra_tentativa = input('Por favor, digite uma palavra válida: ') #valida palavra do usuario


        for e in palavra_tentativa:
            if e not in 'abcdefghijklmnopqrstuvwxyz':
                palavra_tentativa = input('\nDigite uma palavra aleatória com 5 letras: ')

        print()
        print(palavra_usuario(palavra_tentativa))
        
        
#------------------------------------------------------------ verifica letras ----------------------------------------------------------------------------------
        lista_quadrados = ['⬜','⬜','⬜','⬜','⬜']

        for i in range(0,5):
            if palavra_tentativa.count(palavra_tentativa[i]) > 1 and palavra_tentativa[i] != ' ':
                if palavra_tentativa[i] == palavra_tentativa[i-1]:
                    lista_quadrados[i] == '🟩'
                elif palavra_tentativa[i] == palavra_jogo[i]:
                    lista_quadrados[i] = '🟩'
                    palavra_tentativa = palavra_tentativa.replace(palavra_tentativa[i], ' ')
                elif palavra_tentativa[i] not in palavra_jogo:
                    lista_quadrados[i] = '⬜'
                elif palavra_tentativa[i] != palavra_jogo[i]:
                    lista_quadrados[i] = '🟨'
                    palavra_tentativa = palavra_tentativa.replace(palavra_tentativa[i], ' ')
                else:
                    lista_quadrados[i] = '⬜'

            elif palavra_tentativa.count(palavra_tentativa[i]) <= 1:

                if palavra_tentativa[i] in palavra_jogo:

                    if palavra_tentativa[i] == palavra_jogo[i]:

                        lista_quadrados[i] = '🟩'
                        
                        if i < 4:
                            if palavra_tentativa[i] == palavra_tentativa[i+1]:
                                continue

                    elif palavra_tentativa[i] != palavra_jogo[i]:
                        lista_quadrados[i] = '🟨'
                        if i < 4:
                            if palavra_tentativa[i] == palavra_tentativa[i+1]:
                                continue

                elif palavra_tentativa[i] not in palavra_jogo:
                    lista_quadrados[i] = '⬜'
                    if i < 4:
                            if palavra_tentativa[i] == palavra_tentativa[i+1]:
                                continue



        resultado = ''.join(lista_quadrados)
        print(resultado)
        contador_tentativas -= 1

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

        if resultado == '🟩🟩🟩🟩🟩': #ganha jogo
            if contador_tentativas == 1:
                print_slow(f'\nParabéns! Você acertou a palavra em {6 - contador_tentativas} tentativa!')
            else:
                print_slow(f'\nParabéns! Você acertou a palavra em {6 - contador_tentativas} tentativas!')
            time.sleep(1)

            reiniciar = input('\nVocê gostaria de reiniciar o jogo? Digite "s" caso sim ou "n" caso não: ') #desejo de reiniciar
            if reiniciar == 's':
                break
            elif reiniciar == 'n':
                print_slow('Até a próxima, jogador!')
                time.sleep(1)
                exit()
            while reiniciar != 's' and reiniciar != 'n':
                reiniciar = input('\nVocê gostaria de reiniciar o jogo? Digite "s" caso sim ou "n" caso não: ')

        elif contador_tentativas == 0: #as tentaticas se esgotam
            print_slow(f'\nAh não! Infelizmente suas tentativas esgotaram, jogador... A palavra correta era "{palavra_jogo.upper()}".')
            time.sleep(1)
            reiniciar = input('\nVocê gostaria de reiniciar o jogo? Digite "s" caso sim ou "n" caso não: ')
            if reiniciar == 's':
                break
            elif reiniciar == 'n':
                print_slow('Até a próxima, jogador!')
                time.sleep(1)
                exit()
