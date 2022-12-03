user = input('Elige: Piedra, Papel o Tijera => ')
computer_option = 'Piedra'

if user  == computer_option:
    print('Empate!')
    
elif user == 'Piedra':
    if computer_option == 'Tijera':
        print('Piedra gana a Tijera')
        print('Ganaste! 🎉')
    else:
        print('Papel gana a Piedra')
        print('Computer Gano! 🥲')
        
elif user == 'Papel':
    if computer_option == 'Piedra':
        print('Papel gana a Piedra')
        print('Ganaste! 🎉')
    else:
        print('Tijera gana a Papel')
        print('Computer Gano! 🥲')
        
elif user == 'Tijera':
    if computer_option == 'Papel':
        print('Tijera gana a Papel')
        print('Ganaste! 🎉')
    else:
        print('Piedra gana a Tijera')
        print('Computer Gano! 🥲')