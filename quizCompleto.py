print('''
Q1 - No Python, como se chama uma 'caixa' uasada para armazenar dados?
a - texto
b - variavel
c - uma caixa de sapato
''')
resposta = input().lower()

if resposta == "a":
    print("Não - texto e um tipo de dado :( ")
elif resposta == "b" :
    print("Correto!!:) ")
elif resposta == "c" :
    print("Não seja bobinho! :( ")
else:
    print("Você não escolheu a, b ou c :( ")
