pontos = 0
print("Vamos jogar? Vc tem 0 pontos")
print('''
Q1 - Qual o melhor time do Brasil?
a - Flamento
b - Gama
c - Corinthians
d - São Paulo
e - Botafogo
''')
q1 = input().lower()

if q1 == "a":
    pontos = pontos + 1
else:
    print("Resposta errada")

print('''
Q2 - Qual o melhor cantor(a) do Brasil?
a - Luan Santana
b - Toquinho
c - Anita
d - Xuxa
e - Jorge e Matheus
''')
q2 = input().lower()

if q2 == "e":
    pontos = pontos + 1
else:
    print("Resposta errada")

print('''
Q3 - Qual esporte queima mais calorias?
a - Futebol
b - Squash
c - Natação
d - Tênis
e - Queimada
''')
q3 = input().lower()

if q3 == "b":
    pontos = pontos + 1
else:
    print("Resposta errada")

print("Sua pontuação foi:",pontos,"pontos")
