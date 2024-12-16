# List array
marks = [12,23,44,56,88,33] #element 1,2,3,4,5,6

print(f'marks type is: {type(marks)}')
print(f'total {len(marks)} marks')

#print list value
print(marks[1]) #23 mark list index
print(marks[0])
print(marks[-1]) #33
print(marks[2:5]) # [44,56,88]

#how to edit value in list array
marks[0] = 77
print(marks[0])

#add list element
marks.append(95) #adding list
print(marks)

marks.insert(1,30)
print(marks)

#remove list element
marks.remove(44) #delete just one index
print(marks)

marks.pop(2) #delete element
print(marks)

marks.clear()
print(marks)

#for loop
studentMarks = [77, 30, 23, 44, 56, 88, 33, 95]
studentMarks1 = []
for mark in studentMarks:
    print([mark])

for mark in studentMarks1:
    print([mark])
else:
    print('no info')

#assignment while loop print list can?
i = 0
while (i <len(studentMarks)):
    print(studentMarks[i])
    i=i+1