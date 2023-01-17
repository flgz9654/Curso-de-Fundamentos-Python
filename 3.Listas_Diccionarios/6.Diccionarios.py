my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'Francisco',
    'last_name': 'Garcia Zuluaga',
    'age': '28'
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('name'))

print('avion' in my_dict)
print('name' in my_dict)

# Insert & Update Dict

person = {
    'name': 'Francisco',
    'last_name': 'Garcia',
    'langs': ['python', 'javascript'],
    'age': 28
}

print(person)

person['name'] = 'Luis'
person['age'] -= 10
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age')
print(person)

print('Items')
print(person.items())

print('Keys')
print(person.keys())

print('Values')
print(person.values())