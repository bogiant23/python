#getting help
print(help(len))

#mendefinisikan fungsi
def least_difference(a,b,c):
    diff1=abs(a-b)
    diff2=abs(b-c)
    diff3=abs(a-c)
    return min(diff1,diff2,diff3)

#parameter or arguments
#default parameter
def greet():
    print('Hello, colin')

def greet(who="colin"):
    print("hello,", who)

print(greet())

print(greet("Fauzan"))

#keyword parameter
def fungsi_04(nama):
    print(nama)
fungsi_04(nama='rudi')

#arbitary parameter
#contoh fungsi args
def fungsi_05 (*nama):
  for item in nama:
    print(item)


fungsi_05('rudi','santi','mirna')

#contoh fungsi kwargs
def fungsi_06 (**nama):
  for key, value in nama.items():
    print(key, value)

fungsi_06(nama = 'rudi', umur = 18)

#Fungsi Lambda
kali_2 = lambda x: x * 2

print(kali_2(2))

#map
data = [1,2,3,4]

def kali_3(nilai):
  return nilai*3

hasil = list(map(kali_3,data))

print(hasil)

data = [1,2,3,4]

hasil = list(map(lambda x:x*3,data))

print(hasil)