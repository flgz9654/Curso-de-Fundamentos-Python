
# Loop While

counter = int(input('Digita un numero menor a 30: '))

while counter < 30:
    counter += 1
    if counter < 15:
        break
    print(counter)
    
while counter < 30:
    result = counter % 2
    if result == 0:
        break
    print('Numero par', counter)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for element in numbers:
    result = element % 2
    if result == 0:
        print('Numero Par =>', element)
    if result != 0:
        print('Numero Impar =>', element)
        
        
# Loop For

family = [
    
    {'name': 'Francisco',
     'age': '28',
     'job': 'Desarrollador',
     'parentesco': 'principal',
    },
    
    {'name': 'Paula',
     'age': '28',
     'job': 'Comunicadora',
     'parentesco': 'Novia',
    },
    
    {'name': 'Andres',
     'age': '43',
     'job': 'Comerciante',
     'parentesco': 'Hermano',
    },
    
    {'name': 'Diana',
     'age': '39',
     'job': 'Influencer',
     'parentesco': 'Hermana',
    }
]

for element in family:
    print('Job =>', element['job'])