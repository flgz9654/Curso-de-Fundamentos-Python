name = 'Francisco'
last_name = 'Garcia Zuluaga'
my_age = 28
print(name)
print(last_name)
print(my_age)

full_name = name + ' ' + last_name + ' ' + str(my_age)
print(full_name)

quote = "I'am Francisco"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

# Format

template = 'Hola, mi nombre es ' + name + ' ' + last_name + ' y mi edad es ' + str(my_age)
print('v1', template)

template = 'Hola, mi nombre es {} {} y mi edad es {}'.format(name, last_name, my_age)
print('v2', template)

template = f'Hola, mi nombre es {name} {last_name} y mi edad es {my_age}'
print('v3', template)