#membuat list
#list berisi koleksi nilai/data
#inisialisasi suhung anggota keluarga
suhu1 = 21
suhu2 = 20
suhu3 = 22

#simpan dalam list
suhu_keluarga= [suhu1, suhu2, suhu3]

print(suhu_keluarga[1])

#list bisa berisi tipe data apapun dan tidak harus semua data berisi tipedata yang sama

#membuat list
suhu_keluarga_ucup = ['ayah ucup', 19,'ucup',19, 'ibu ucup', 20]
suhu_keluarga_boy = ['ayah boy', 20, 'anak boy', 18]
#membuat list dalam list dan dicampur dengan data boolean
suhu_keluarga = [suhu_keluarga_ucup, suhu_keluarga_boy, True]

#Akses data list
tinggi_badan = [162,177,182,150,166]

#print posisi pertama
print(tinggi_badan[0])

#print posisi kedua dari belakang
print(tinggi_badan[-2])

#mengambil data dengan index 0,1,2,3
print(tinggi_badan[:4])

#mengambil data dengan index 2,3,4
print(tinggi_badan[2:5])

#manupulasi list
#mengubah suhu ucup
suhu_keluarga_ucup[3]= 22
print(suhu_keluarga_ucup)

#mengganti ibu ucup dengan mamah ucup
suhu_keluarga_ucup[-2:] = ['mamah ucup', 22]
print(suhu_keluarga_ucup)

#menambahkan element dalam list
suhu_keluarga_ucup=suhu_keluarga_ucup+['adik ucup', 20]
print(suhu_keluarga_ucup)

#menambahkan elemen dalam list, bisa menggunakan .append() atau .insert()
murid = ['ayu', 'bagus', 'fajar','cahyo','ani']
murid.append('rizky')
print(murid)
murid.insert(2,'ahmad')
print(murid)

#mendelete list
del(suhu_keluarga_ucup[0])
print(suhu_keluarga_ucup)

#menghapus elemen menggunakan remove dan pop
murid.pop(2)
print(murid)

#menghapus menggunakan remove
murid.remove('cahyo')
print(murid)