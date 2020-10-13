import random


char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

largo = int(input('Introduzca la longitud de la contraseña:'))
passw = ''
for c in range(largo):
    passw += random.choice(char)
print(passw)