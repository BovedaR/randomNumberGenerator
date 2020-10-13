import random


caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

long = int(input('Introduzca la longitud de la contraseña:'))
password = ''
for c in range(long):
    password += random.choice(caracteres)
print(password)