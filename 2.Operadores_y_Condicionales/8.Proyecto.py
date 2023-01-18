import  random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:
    
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    
    user = input('Elige: piedra, papel o tijera => ')
    user = user.lower()
    
    rounds += 1

    if not user in options:
        print('Esa opcion no es valida')
        continue

    computer_option = random.choice(options)

    print('User Option =>', user)
    print('Computer Option =>', computer_option)

    if user  == computer_option:
        print('Empate!')
        
    elif user == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('Ganaste! 🎉')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('Computer Gano! 🥲')
            computer_wins += 1
            
    elif user == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('Ganaste! 🎉')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('Computer Gano! 🥲')
            computer_wins += 1
            
    elif user == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('Ganaste! 🎉')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Computer Gano! 🥲')
            computer_wins += 1
    
    if computer_wins == 2:
        print('El ganador final es Computer')
        break
    
    if user_wins == 2:
        print('El ganador final es User')
        break