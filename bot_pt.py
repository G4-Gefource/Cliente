#  CHATBOT

import os
import msvcrt
import funcoes


def chat():
    func = True
    while func is True:
        print('Olá! Eu sou o 🤖BOT🤖, vou te ajudar a escolher o ponto que te dará a melhor experiência!')
        num = input('Primeiro me diga, você está viajando sozinho?\n(S - Sim/N - Não)\n')
        if (num[0]).upper() == 'S':
            print('Perfeito! Com quem você está viajando?')
            print('1 - Em família')
            print('2 - Com amigos')
            print('3 - Em casal')
            op = int(input('Selecione uma das opções e tecle ENTER: '))
        elif (num[0]).upper() == 'N':
            print('Perfeito! Agora fala um pouco da sua disponibilidade de horário!')
            print('1 - Manhã')
            print('2 - Tarde')
            print('3 - Noite')
            op = int(input('Selecione uma das opções e tecle ENTER: '))
        else:
            print('Desculpe, não entendi, pressione qualquer tecla para voltar ao início.')
            char = msvcrt.getch()
            funcoes.limpa()
