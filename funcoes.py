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
    print('2 - Dar feedback sobre visita\n')
    print('3 - Dar feedback sobre o hotel\n')
    print('4 - Dar feedback sobre o Eventum\n')
    print('0 - Sair\n')


def menu_es():  # FUNÇÃO PARA MENU EM ESPANHOL
    print('1 - Encontrar lugares de interés\n')
    print('2 - Dar su opinión sobre la visita\n')
    print('3 - Dar su opinión sobre el hotel\n')
    print('4 - Dar su opinión sobre el Eventum\n')
    print('0 - Salir\n')
