import os
os.system("CLS")

arquivo = open('pontos.txt', 'a')
arquivo.write("Olá Mundo!")

arquivo = open('pontos.txt', 'r')
print(arquivo.read())
