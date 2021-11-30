numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])

#mengubah nilai dalam dictionary
numbers['one'] = 'satu'
print(numbers)

for k in numbers:
    print("{} = {}".format(k, numbers[k]))


for key in numbers.values():
    print("{}".format(key))


for key, value in numbers.items():
    print("{} = {}".format(key, value))

#mengecek apakah suatu key tertentu ada dalam dictionary
'one' in numbers

numbers = {'one':1, 'two':2, 'three':3}
numbers['four'] = 10
print(numbers)

numbers1 = {'two':5}
numbers.update(numbers1)
print(numbers)



numbers = {'four': 10, 'one': 1, 'three': 3, 'two': 5}
numbers.pop('one')
print(numbers)

numbers.clear()
print(numbers)

numbers = {'four': 10, 'three': 3, 'two': 5}
del numbers['four']
print(numbers)

del numbers
print(numbers)
