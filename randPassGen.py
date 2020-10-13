import random


caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

long = int(input('Introduzca la longitud de la contraseña:'))
contraseña = ''
for c in range(long):
    contraseña += random.choice(caracteres)
print(contraseña)