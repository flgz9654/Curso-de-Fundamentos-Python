if True:
    print('Deberia ejecutarse')
    
if False:
    print('Nunca se ejecuta')


# pet = input('Cual es tu mascota favorita? ')

# if pet == 'Perro':
#     print('Grandioso tienes buen gusto')
# elif pet == 'Gato':
#     print('Espero tengas suerte')    
# elif pet == 'Pez':
#     print('Eres lo maximo')
# else:
#     print('No tienes ninguna mascota interesante')


'''
stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
    print('El stock es correcto')
else:
    print('El stock es incorrecto')
'''

number = int(input('Ingresa un numero para validar: '))
result = number % 2

if (result == 0):
    print('El numero ingresado es par')
else:
    print('El numero ingresado es impar')
