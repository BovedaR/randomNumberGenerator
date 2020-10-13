import random

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

long = int(input('Introduzca la longitud de la contraseña:'))
contraseña = ''.join([random.choice(caracteres) for _ in range(long)])
print(contraseña)
