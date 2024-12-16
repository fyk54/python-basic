#dictionary = object

student = {
    "name:": 'eric',
    "age:" : 28,
    "passed Exam:" : False
}
#key-value pair
print(f'student is{type(student)}, lenght is {len(student)}')

#read dictionary value
print(student["name:"])
#add and update new pair in dictionary
student["teacher"] = 'paul'

student["age"] = 21
print(f'add new pair key: {student}')

#delete key value pair
student.pop('teacher')
print(f'delete pair key: {student}')

#For loop go via dictionary

for info in student:
    print(info)

for info in student:
    print(info, student[info])

#exam
pythonClass = [
    {"name":'Daisy',"age":20,"passedExam":False},
    {"name":'Peter',"age":19,"passedExam":True},
    {"name":'Patrick',"age":20,"passedExam":True},
    {"name":'Lulu',"age":22,"passedExam":True}
]

print(f'name\tage\tpassedExam')
for exam in pythonClass:
    
    #another way
    """   passed = 'fail'
    if exam["passedExam"]:
        passed = 'pass' """

    passed = 'pass'if exam["passedExam"] else 'fail'

    #print(f'{exam["name"]}\t{exam["age"]}\t{exam["passedExam"]}')
    print(f'{exam["name"]}\t{exam["age"]}\t{passed}')
 
