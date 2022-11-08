import os
import msvcrt

# FUNÇÕES


def limpa():  # FUNÇÃO PARA LIMPAR A TELA
    os.system("cls")


def pausa_pt():  # FUNÇÃO PARA PAUSAR O SISTEMA EM PORTUGUÊS
    print('\nPressione qualquer tecla para continuar...\n')
    char = msvcrt.getch()


def pausa_es():  # FUNÇÃO PARA PAUSAR O SISTEMA EM ESPANHOL
    print('\nPulse cualquier tecla para continuar...\n')
    char = msvcrt.getch()


def menu_pt():  # FUNÇÃO PARA MENU EM PORTUGUÊS
    print('1 - Encontrar pontos turísticos\n')
    print('2 - Dar feedback sobre o hotel\n')
    print('3 - Dar feedback sobre o Eventum\n')
    print('0 - Sair\n')


def menu_es():  # FUNÇÃO PARA MENU EM ESPANHOL
    print('1 - Encontrar lugares de interés\n')
    print('2 - Dar su opinión sobre el hotel\n')
    print('3 - Dar su opinión sobre el Eventum\n')
    print('0 - Salir\n')

    
    def exibe_ponto_pt(ponto):  # FUNÇÃO PARA EXIBIR PONTO TURÍSTICO EM PORTUGUÊS
    print(
        f'Acho que o passeio perfeito para vocês seria o {(ponto["NOME"]).title()}!')
    print(
        f'O {(ponto["NOME"]).title()} tem uma nota de {ponto["NOTA"]} nos sites de avaliação!')
    print(
        f'Além disso, você o encontra a {ponto["LOCALIZAÇÃO"]} do hotel!')


def exibe_ponto_es(ponto):  # FUNÇÃO PARA EXIBIR PONTO TURÍSTICO EM ESPANHOL
    print(
        f'¡Creo que el tour perfecto para ti sería el {(ponto["NOME"]).title()}!')
    print(
        f'¡El {(ponto["NOME"]).title()} tiene una nota de {ponto["NOTA"]} en los sitios de revisión!')
    print(
        f'¡Además, puedes encontrar {ponto["LOCALIZAÇÃO"]} del hotel!')
