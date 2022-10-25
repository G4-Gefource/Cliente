import os
os.system("CLS")

arquivo = open('pontos.txt', 'a')
arquivo.write("Hello World!")

arquivo = open('pontos.txt', 'r')
print(arquivo.read())
