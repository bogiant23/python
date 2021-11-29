#inisiasi satu-satu
a=1
b=2
c=3

#inisiasi banyak
d, e, f = 4, 5, 6

#inisiasi bernilai sama
g =h =i =7

#untuk mencetak hasil
print ('a:', a)
print ('b:', b)
print ('c:', c)
print ('d:', d)
print ('e:', e)
print ('f:', f)
print ('g:', g)
print ('h:', h)
print ('i:', i)


#integer
x = 2
print(x)
type(x)

#float
x = 2.5
print(x)
type(x)

#string
a = 'hello'
b = "hello 2"
print(a)
print(b)
type(a)
type(b)

#boolean
c = True
d = False
print(c)
type(c)

#Printing
name = 'Budi'
age = 17
print('Hello i am ' + name + ' i am ' + str(age) + ' years old')
print('Hello i am ', name, ' i am ' ,age, ' years old')

#Selain cara diatas, kita bisa menggunakan string formatting seperti berikut:

# Old Style
print('Hello i am %s i am %d years old' % (name, age))
# 'New Style' string formatting
print('Hello i am {0} i am {1} years old'.format(name, age))
# String interpolation
print(f'Hello i am {name} i am {age} years old')

 # Aritmatika
A = 12
B = 2
C = A + B
D = A / B
print(C)
print(D)

#Mengubah float menjadi int
D = int(A / B)
print(D)