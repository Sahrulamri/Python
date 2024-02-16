# operasi komparasi
# lebih besar dari >
a =3 
b =5
# lebih besar dari 
print('================ lebih besar dari')
hasil = a > 3
print(a, ' > ', 3, ' = ', hasil)
hasil = b > 3
print(b, ' > ', 3, ' = ', hasil)
# kurang dari 
print('================ kurang dari')
hasil = a < 3
print(a, ' < ', 3, ' = ', hasil)
hasil = b < 3
print(b, ' < ', 3, ' = ', hasil)

# lebih dari sama dengan
print('================ lebih dari sama dengan')
hasil = a >= 3
print(a, ' >= ', 3, ' = ', hasil)
hasil = b >= 3
print(b, ' >= ', 3, ' = ', hasil)

# kurang dari sama dengan
print('================ kurang dari sama dengan')
hasil = a <= 3
print(a, ' <= ', 3, ' = ', hasil)
hasil = b <= 3
print(b, ' <= ', 3, ' = ', hasil)

#  sama dengan
print('================  sama dengan')
hasil = a == 3
print(a, ' == ', 3, ' = ', hasil)
hasil = b == 3
print(b, ' == ', 3, ' = ', hasil)
hasil = b == a
print(b, ' == ', 3, ' = ', hasil)

#  tidak sama dengan
print('================ tidak sama dengan')
hasil = a != 3
print(a, ' != ', 3, ' = ', hasil)
hasil = b != 3
print(b, ' != ', 3, ' = ', hasil)
hasil = b != a
print(b, ' != ', 3, ' = ', hasil)

# is sebagai komparasi object identity
print('================ object identity is')
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x = ", x, " id = ", hex(id(x)));
print("nilai y = ", y, " id = ", hex(id(y)));
hasil = x is y
print( 'x is y = ', hasil )

print('================ object identity is not')
x = 5 # ini adalah assigment membuat object
y = 8
print("nilai x = ", x, " id = ", hex(id(x)));
print("nilai y = ", y, " id = ", hex(id(y)));
hasil = x is not y
print( 'x is not y = ', hasil )
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x = ", x, " id = ", hex(id(x)));
print("nilai y = ", y, " id = ", hex(id(y)));
hasil = x is not y
print( 'x is not y = ', hasil )
x = 5 # ini adalah assigment membuat object
y = 8
print("nilai x = ", x, " id = ", hex(id(x)));
print("nilai y = ", y, " id = ", hex(id(y)));
hasil = x is not y
print( 'x is not y = ', hasil )