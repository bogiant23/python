#membuat tuple

tuple_01 = (1,2,3,4)
tuple_02 = (1,)

#mengakses index positif
print(tuple_01[1])

#mengakses index negatif
print(tuple_01[-1])

#memotong & menduplikasi tuple
tuple_03 = tuple_01[0:2]
tuple_04 = tuple_01[:]

print(tuple_03)
print(tuple_04)

#Menginisiasi Multi-Variabel Menggunakan Tuple
tuple_01 = (1,2,3,4)

#sekarang akan kita masukkan kedalam 4 variabel dikarenakan tuple tersebut memiliki 4 anggota
a, b, c, d = tuple_01

print(a, b, c, d)
print(type(a), type(b), type(c), type(d))