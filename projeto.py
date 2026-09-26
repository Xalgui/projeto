import random

tamanho =int(input('digite o tamanho da senha'))

letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
simbulos = "!@#$%&*"
numero = "0123456789"

tamanho = 15

senha = ''

for i in range(tamanho):
    sorteado = random.choice(letras_minusculas)



