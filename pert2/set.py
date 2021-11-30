set_01 = {4,5,6,2}

print(set_01)

set_02 = set()
set_03 = set([2,1,4,3])

print(type(set_02))
print(set_03)

#Menghapus Anggota Set
set_01 = {4,5,6,2}

#menggunakan discard()
set_01.discard(4)
print(set_01)

#menggunakan remove()
set_01.remove(2)
print(set_01)

#Mengubah & Menambah Anggota Set
set_04 = {2,3,4,5,6}

set_04.add(1)
print(set_04)

#update
set_04.update([4,7,8])

print(set_04)

set_04.add(10)
print(set_04)


#operasi pada set
Set_A = {1,2,3,4}
set_B = {3,4,5,6}

#union
print(set_A|set_B)
print(set_A.union(set_B))

#intersection
print(set_A & set_B)
print(set_A.intersection(set_B))

#difference
print(set_A - set_B)
print(set_A.difference(set_B))

#symmetric_difference
print(set_A ^ set_B)
print(set_A.symmetric_difference(set_B))