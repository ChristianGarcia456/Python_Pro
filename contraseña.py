import random

caracteres_contrasena = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud_contrasena = int(input("ingrese la longitud de la contraseña: "))
contrasena = ""
for i in range (longitud_contrasena):

    contrasena += random.choice(caracteres_contrasena)
    

print(f'hola esta es tu contrasena{contrasena}')