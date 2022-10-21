#  CHATBOT

import os
import msvcrt
import funcoes


def chat():
    func = True
    while func is True:
        print('¡Hola! ¡Soy el 🤖BOT🤖, te ayudaré a elegir el punto que te brindará la mejor experiencia!')
        num = input('Primero dime, ¿viajas solo?\n(S - Sí/N - No)\n')
        if (num[0]).upper() == 'S':
            print('¡Perfecto! ¿Con quién viajas?')
            print('1 - En familia')
            print('2 - Con amigos')
            print('3 - En pareja')
            op = int(input('Seleccione una de las opciones y presione ENTER: '))
        elif (num[0]).upper() == 'N':
            print('¡Perfecto! ¡Ahora hable un poco sobre su disponibilidad de tiempo!')
            print('1 - Mañana')
            print('2 - Tarde')
            print('3 - Noche')
            op = int(input('Seleccione una de las opciones y presione ENTER: '))
        else:
            print('Lo siento, no entiendo, pulsa cualquier tecla para volver al principio.')
            char = msvcrt.getch()
            funcoes.limpa()
