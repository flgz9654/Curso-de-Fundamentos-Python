name = "Franisco"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Francisco" + " Garcia")
print(10 + 20)
print("Francisco" + " 15")

age = 28 
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

# Todo lo que se pide por pantalla input lo recibe como str
# Con int puedes cambiar el tipo de dato
age = int(input("Escribe tu edad => "))
print(type(age))
# age = int(age)
age += 10
print(f"Tu edad en 10 años sera {age}")
