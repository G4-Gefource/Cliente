# PRIMEIRO PROTÓTIPO DA VERSÃO DE APP DO CLIENTE DO EVENTUM

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

# INÍCIO DO CÓDIGO

auxiliar = True
while auxiliar is True:
    limpa()
    print('Informe o voucher recebido em seu checkin:')
    print('Informar el voucher recibido en el check-in:')
    voucher = int(input(''))
    if voucher == 000:
        op = 1  # VARIÁVEL AUXILIAR PARA LAÇO DE REPETIÇÃO
        while op != 0:
            limpa()
            print('Bem vindo ao Eventum!')
            print('Bienvenido al Eventum!')
            print('\nGostaria da versão em espanhol?')
            print('¿Te Gustaria la version en español?')
            # UPPER() -> TRANSFORMA TODAS OS CARACTERES INSERIDOS EM MAIÚSCULO
            idioma = input('S - Sim(Sí)\nN - Não(No)\n').upper()
            limpa()

            if idioma[0] == 'N':  # COMPARA APENAS A PRIMEIRA LETRA ESCRITA PELO USUÁRIO
                print('Você selecionou a opção em Português!\n')
                opt = 1
                while opt != 0:
                    menu_pt()   # CHAMA A FUNÇÃO MENU_PT
                    opt = int(input('Selecione uma das opções e tecle ENTER: '))
                    limpa()
                    if opt == 1:
                        aux = 1
                        while aux != 0:
                            pt = input('Você já sabe o tipo de ponto turístico que está procurando?\n(S - Sim/N - Não)\n')
                            if (pt[0]).upper() == 'S':
                                print('Jóia.')
                                aux = int(input('Pressione 0 para sair: '))
                                limpa()
                            elif (pt[0]).upper() == 'N':
                                print('Puts cara.')
                                aux = int(input('Pressione 0 para sair: '))
                                limpa()
                            else:
                                print('Opção inválida.')
                                aux = int(input('Pressione 0 para sair: '))
                                limpa()
                    elif opt == 2:
                        print('Informe o ponto turístico registrado que deseja dar feedback.')
                    elif opt == 3:
                        print('Informe o hotel em que ficou hospedado.')
                    elif opt == 4:
                        print('Deixe aqui seu Feedback do Eventum.')
                    elif opt == 0:
                        print('Obrigado por usar o Eventum!')
                        pausa_pt()
                        op = 0
                        auxiliar = False
                    else:
                        print('Opção inválida.')
                        pausa_pt()
                        limpa()
            elif idioma[0] == 'S':  # COMPARA APENAS A PRIMEIRA LETRA ESCRITA PELO USUÁRIO
                print('¡Ha seleccionado la opción en Español!')
                opt = 1
                while opt != 0:
                    menu_es()   # CHAMA A FUNÇÃO MENU_ES
                    opt = int(input('Seleccione una de las opciones y presione ENTER: '))
                    if opt == 1:
                        aux = 1
                        while aux != 0:
                            pt = input('¿Ya sabes el tipo de lugar turístico que estás buscando?\n(S - Sí/N - No)\n')
                            if (pt[0]).upper() == 'S':
                                print('Joya.')
                                aux = int(input('Pulsa 0 para salir: '))
                                limpa()
                            elif (pt[0]).upper() == 'N':
                                print('Dios mio.')
                                aux = int(input('Pulsa 0 para salir: '))
                                limpa()
                            else:
                                print('Opción no válida.')
                                aux = int(input('Pulsa 0 para salir: '))
                                limpa()
                    elif opt == 2:
                        print('Informe el lugar turístico registrado que desea registrar.')
                    elif opt == 3:
                        print('Informe al hotel donde se hospedó.')
                    elif opt == 4:
                        print('Deja tus comentarios de Eventum aquí.')
                    elif opt == 0:
                        print('¡Gracias por usar Eventum!')
                        pausa_es()
                        op = 0
                        auxiliar = False
                    else:
                        print('Opción no válida.')
                        pausa_es()
                        limpa()
            else:
                print('Opção inválida inserida.')
                print('Opción no válida ingresada.')
                print('Pressione qualquer tecla para continuar...\n')
                print('Pulse cualquier tecla para continuar...\n')
                char = msvcrt.getch()
    else:
        print('Este voucher não é válido, por favor tente novamente.')
        print('Se o problema persistir entre em contato com um funcionário do hotel.')
        print('\nEste voucher no es válido, inténtalo de nuevo.')
        print('Si el problema persiste, comuníquese con un empleado del hotel.')
        print('\nPressione qualquer tecla para continuar...\n')
        print('Pulse cualquier tecla para continuar...\n')
        char = msvcrt.getch()
