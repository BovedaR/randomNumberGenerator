import random
print(''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789') for _ in range(int(input('Introduzca la longitud de la contraseña:')))]))
