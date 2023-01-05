# Operador in para verificar sin un string se encuentra en otro string

text = 'Ella sabe programar en Python'

# print('JavaScript' in text)
# print('Python' in text)

# if 'Python' in text:
#     print('Elegiste bien!!')
# else:
#     print('Tambien elegiste bien')
    
    
# Metodos para manipular strings

size = len(text) # Contar los caracteres en un string
print(size)
print(text)
print(text.upper()) # Convertir string mayuscula
print(text.lower()) # Convertir string minuscula
print(text.capitalize()) # Convertir el string con primera letra en mayusc
print(text.count('a')) # Contar string
print(text.swapcase()) # Alternar mayusc por minusc
print(text.startswith('Ella')) # True or False si el texto inicia con un string especifico
print(text.endswith('Rust')) # True or False si el texto finaliza con un string especifico
print(text.replace('Python', 'JavaScript')) # Reemplazar un string por otro

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize()) # String con primera letra en mayusc
print(text_2.title()) # String para convertir en mayusc la primera letra
print(text_2.isdigit()) # Validar si el string es un digito
print('398'.isdigit()) # Validar si el string es un digito

text_3 = input("Registra tu nombre: ")
print(text_3.title())
