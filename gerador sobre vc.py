from random import *

print("Gerador de Cumprimentos")
print("----------------------")

adjetivos = [ "maravilhoso" , "acima da média" , "exelente"]
hobbies = [ "andar de bicicleta" , "programa" , "fazer chá" ]

nome = input("Qual é o seu nome?: ")
print("Aqui está o seu cumprimento" , nome , ":" )

print(nome , "voçê é" , chice(adjetivos) , "em" , choice(hobbies))
print("De nada!")
             
            
