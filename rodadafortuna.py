from random import *

print('''
Porta da Fortuna!
=========

Existe uma super prêmio atrás de uma destas 3 portas!
Adivinhe qual e a porta certa para ganha o prêmio!

     ____       ____     ____
    |    |     |    |   |    |
    |[1] |     |[2] |   |[3] |
    |   0|     |   0|   |   0|
    |____|     |____|   |____|  

Escolha uma porta (1,2 ou 3)
''')

portaEscolhida = input()
portaEscolhida = int(portaEscolhida)

portaCerta = randint(1,3)

print("A porta escolhida foi a",portaEscolhida)
print("A porta certa é a",portaCerta)

if portaEscolhida == portaCerta:
    print("Parabéns!")
else:
    print("Que Peninha!") 
