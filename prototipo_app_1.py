# PRIMEIRO PROTÓTIPO DA VERSÃO DE APP DO CLIENTE DO EVENTUM

import os
import msvcrt
import funcoes  # CHAMA AS FUNÇÕES PARA O PROJETO
import bot_pt
import bot_es

# INÍCIO DO CÓDIGO


auxiliar = True
while auxiliar is True:
    funcoes.limpa()
    print('Bem vindo ao Eventum!')
    print('Bienvenido al Eventum!')
    print('\nGostaria da versão em espanhol?')
    print('¿Te Gustaria la version en español?')
    # UPPER() -> TRANSFORMA TODAS OS CARACTERES INSERIDOS EM MAIÚSCULO
    idioma = input('S - Sim(Sí)\nN - Não(No)\n').upper()
    funcoes.limpa()
    if idioma[0] == 'N':
        op = 1  # VARIÁVEL AUXILIAR PARA LAÇO DE REPETIÇÃO
        while op != 0:
            print('Você selecionou a opção em Português!\n')
            print('Informe o voucher recebido em seu checkin:')
            voucher = input('')
            funcoes.limpa()
            if voucher == '000':  # COMPARA APENAS A PRIMEIRA LETRA ESCRITA PELO USUÁRIO
                opt = 1
                while opt != 0:
                    funcoes.menu_pt()   # CHAMA A FUNÇÃO MENU_PT
                    opt = int(input('Selecione uma das opções e tecle ENTER: '))
                    funcoes.limpa()
                    if opt == 1:
                        aux = 1
                        while aux != 0:
                            pt = input(
                                'Você já sabe o tipo de ponto turístico que está procurando?\n(S - Sim/N - Não)\n')
                            funcoes.limpa()
                            if (pt[0]).upper() == 'S':
                                print('👍Jóia.')
                                aux = int(input('Pressione 0 para sair: '))
                                funcoes.limpa()
                            elif (pt[0]).upper() == 'N':
                                print(
                                    'Gostaria da ajuda do 🤖BOT para garantir uma experiência personalizada para você?')
                                bot = input('(S - Sim/N - Não)\n')
                                if (bot[0]).upper() == 'S':
                                    bot_pt.chat()
                                elif (bot[0]).upper() == 'N':
                                    print('')
                                else:
                                    print('Opção inválida.')
                                    funcoes.pausa_pt()
                                    funcoes.limpa()
                            else:
                                print('Opção inválida.')
                                aux = int(input('Pressione 0 para sair: '))
                                funcoes.limpa()
                    elif opt == 2:
                        hotel = 1
                        while hotel != 0:
                            v = ['Como você avalia sua estadia no hotel?', 'Como você avalia seu conforto no hotel?',
                                 'Como você avalia a localização do hotel?', 'Como você avalia a limpeza do hotel?',
                                 'Como você avalia o atendimento dos funcionários?']
                            print('1 - Saint Patrick Praia Hotel')
                            print('2 - Hotel Des Basques')
                            print('3 - Pousada Nossa Casa')
                            print('4 - Saint Patrick Grand Hotel')
                            print('0 - Sair')
                            hotel = int(
                                input(('Informe o hotel em que ficou hospedado: ')))
                            hosped = ''
                            if hotel == 1:
                                hosped = 'Saint Patrick Praia Hotel'
                            elif hotel == 2:
                                hosped = 'Hotel Des Basques'
                            elif hotel == 3:
                                hosped = 'Pousada Nossa Casa'
                            elif hotel == 4:
                                hosped = 'Saint Patrick Grand Hotel'
                            elif hotel == 0:
                                print('Operação encerrada pelo usuário.\n')
                                funcoes.pausa_pt()
                                funcoes.limpa()
                            else:
                                print('Opção inválida.')
                                funcoes.pausa_pt()
                                funcoes.limpa()
                            print(
                                f'Responda às perguntas sobre o hotel {hosped}.\n')
                            soma = 0.0
                            i = 0
                            while i in range(len(v)):
                                print(v[i])
                                a = float(input('Informe uma nota de 0 a 5: '))
                                if a > 5 or a < 0:
                                    print('Esta nota não pode ser inserida.')
                                    i = i - 1
                                else:
                                    soma = soma + a
                                    i = i + 1
                            media = soma / len(v)
                            print(
                                f'Você avaliou o hotel {hosped} com {media:.2f} estrelas.')
                            print(
                                f'Gostaria de deixar um comentário sobre o hotel {hosped}?')
                            av = input('').upper()
                            if av[0] == 'S':
                                coment = input('Informe aqui seu comentário: ')
                            print('Obrigado pela sua avaliação!')
                            hotel = 0
                            funcoes.pausa_pt()
                            funcoes.limpa()
                    elif opt == 3:
                        print('Deixe aqui seu Feedback do Eventum.')
                    elif opt == 0:
                        print('Obrigado por usar o Eventum!')
                        funcoes.pausa_pt()
                        op = 0
                        auxiliar = False
                    else:
                        print('Opção inválida.')
                        funcoes.pausa_pt()
                        funcoes.limpa()
            else:
                print('Este voucher não é válido, por favor tente novamente.')
                print(
                    'Se o problema persistir entre em contato com um funcionário do hotel.')
                funcoes.pausa_pt()
    elif idioma[0] == 'S':
        print('¡Ha seleccionado la opción en Español!\n')
        opt = 1
        while opt != 0:
            print('Informar el voucher recibido en el check-in:')
            voucher = input('')
            funcoes.limpa()
            if voucher == '000':
                funcoes.menu_es()   # CHAMA A FUNÇÃO MENU_ES
                opt = int(
                    input('Seleccione una de las opciones y presione ENTER: '))
                funcoes.limpa()
                if opt == 1:
                    aux = 1
                    while aux != 0:
                        pt = input(
                            '¿Ya sabes el tipo de lugar turístico que estás buscando?\n(S - Sí/N - No)\n')
                        funcoes.limpa()
                        if (pt[0]).upper() == 'S':
                            print('Joya.')
                            aux = int(input('Pulsa 0 para salir: '))
                            funcoes.limpa()
                        elif (pt[0]).upper() == 'N':
                            print(
                                '¿Le gustaría la ayuda de BOT para asegurarle una experiencia personalizada?')
                            bot = input('(S - Sí/N - No)\n')
                            if (bot[0]).upper() == 'S':
                                bot_es.chat()
                            elif (bot[0]).upper() == 'N':
                                print('')
                            else:
                                print('Opción no válida.')
                                funcoes.pausa_es()
                                funcoes.limpa()
                        else:
                            print('Opción no válida.')
                            aux = int(input('Pulsa 0 para salir: '))
                            funcoes.limpa()
                elif opt == 2:
                    hotel = 1
                    while hotel != 0:
                        v = ['¿Cómo califica su estancia en el hotel?', '¿Cómo califica su comodidad en el hotel?',
                             '¿Cómo califica la ubicación del hotel?', '¿Cómo califica la limpieza del hotel?',
                             '¿Cómo califica el servicio de los empleados?']
                        print('1 - Saint Patrick Praia Hotel')
                        print('2 - Hotel Des Basques')
                        print('3 - Pousada Nossa Casa')
                        print('4 - Saint Patrick Grand Hotel')
                        hotel = int(
                            input('Informar al hotel donde se hospedó: '))
                        hosped = ''
                        if hotel == 1:
                            hosped = 'Saint Patrick Praia Hotel'
                        elif hotel == 2:
                            hosped = 'Hotel Des Basques'
                        elif hotel == 3:
                            hosped = 'Pousada Nossa Casa'
                        elif hotel == 4:
                            hosped = 'Saint Patrick Grand Hotel'
                        elif hotel == 0:
                            print('Operación terminada por el usuario.\n')
                            funcoes.pausa_es()
                            funcoes.limpa()
                        else:
                            print('Opción no válida.')
                            funcoes.pausa_es()
                            funcoes.limpa()
                        print(f'Responder preguntas sobre el hotel {hosped}.\n')
                        soma = 0.0
                        i = 0
                        while i in range(len(v)):
                            print(v[i])
                            a = float(input('Introduzca una puntuación de 0 a 5: '))
                            if a > 5 or a < 0:
                                print('Esta nota no se puede ingresar.')
                                i = i - 1
                            else:
                                soma = soma + a
                                i = i + 1
                        media = soma / len(v)
                        print(
                            f'Ha calificado el hotel {hosped} con {media:.2f} estrellas.')
                        print(
                            f'¿Le gustaría dejar una reseña sobre el hotel {hosped}?')
                        av = input('').upper()
                        if av[0] == 'S':
                            coment = input('Ingrese su comentario aquí: ')
                        print('¡Gracias por tu valoración!')
                        hotel = 0
                        funcoes.pausa_es()
                        funcoes.limpa()
                elif opt == 3:
                    print('Deja tus comentarios de Eventum aquí.')
                elif opt == 0:
                    print('¡Gracias por usar Eventum!')
                    funcoes.pausa_es()
                    op = 0
                    auxiliar = False
                else:
                    print('Opción no válida.')
                    funcoes.pausa_es()
                    funcoes.limpa()
            else:
                print('Este cupón no es válido, inténtalo de nuevo.')
                print('Si el problema persiste, comuníquese con un empleado del hotel.')
                funcoes.pausa_es()
    else:
        print('Opção inválida inserida.')
        print('Opción no válida ingresada.')
        print('Pressione qualquer tecla para continuar...\n')
        print('Pulse cualquier tecla para continuar...\n')
        char = msvcrt.getch()
