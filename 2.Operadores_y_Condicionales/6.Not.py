print(not True)
print(not False)

# Negacion con NOT para el AND

print("NOT AND")
print("not True and True => ", not (True and True))
print("not True and False => ", not (True and False))
print("not False and True => ", not (False and False))
print("not False and False => ", not (False and False))

stock = int(input("Ingrese el numero de stock => "))

print(not (stock >= 100 and stock <= 1000))