from random import *

print("Gerador de Cumprimentos 2.0")
print("=======================")

adjetivosFem = ["maravilhosa" , "acima da média" , "incrível", "linda", "forte"]
adjetivosMasc = ["maravilhoso" , "acima da média" , "incrível", "forte", "lindo"]

hobbies = ["ler" , "andar de bicicleta" , "cantar"]

nome = input("Qual o seu nome?")
genero = input("Qual o seu gênero? (M/F)")

print("Aqui está o seu cumprimento", nome, ":")
if(genero == "M"):
    print(nome, "vc é", choice(adjetivosMasc), "em", choice(hobbies))
else:
    print(nome, "vc é", choice(adjetivosFem), "em", choice(hobbies))

print("De nada")
