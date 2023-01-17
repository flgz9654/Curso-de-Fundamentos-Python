import  random

options = ('piedra', 'papel', 'tijera')

user = input('Elige: piedra, papel o tijera => ')
user = user.lower()

if not user in options:
    print('Esa opcion no es valida')

computer_option = random.choice(options)

print('User Option =>', user)
print('Computer Option =>', computer_option)

if user  == computer_option:
    print('Empate!')
    
elif user == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('Ganaste! 🎉')
    else:
        print('papel gana a piedra')
        print('Computer Gano! 🥲')
        
elif user == 'papel':
    if computer_option == 'piedra':
        print('papel gana a piedra')
        print('Ganaste! 🎉')
    else:
        print('tijera gana a papel')
        print('Computer Gano! 🥲')
        
elif user == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('Ganaste! 🎉')
    else:
        print('piedra gana a tijera')
        print('Computer Gano! 🥲')