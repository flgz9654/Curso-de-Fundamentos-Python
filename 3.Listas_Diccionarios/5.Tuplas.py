number = (1, 2, 3, 5)
string = ('nico', 'fran', 'santi', 'fran')
print(number)
print('0 =>', number[0])
print('-1 =>', number[-1])
print(type(number))

print(string)
print(type(string))
print(string.index('fran'))


print(string.count('fran'))

my_list = list(string)
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)