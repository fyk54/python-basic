#Tuple

tup1 = ('people', True, 1997, 2022)

print(tup1[0])
print(type(tup1))

#tuple is set for: element value and order cannot be change.
""" tup1[0] = 'abc' """

tup2 = ('op',) #add , <class 'str'>
print(type(tup2))

import os

path ='C:\\Users\\Eric Fung\\Desktop\\rename\\'

dir = os.listdir(path)

print(type(dir))
print(dir)

print(f'file in have{len(dir)}photo')
newName = input('please enter new file name: ')

for index,filename in enumerate(dir,start = 1):
    "print(index, filename)"
    print(f'now processing:{index}/{len(dir)}page')
    os.rename(path+filename,path+f'{newName}_{index}.jpg')

print(f'finish!!!!!')