num = 0 
"""while (num < 10): #ture
    print('hello')
    num = num + 1
#print hello 10 times"""

mark = input('enter a number:\n')

while (not(mark=='exit')):
    
#intMark = int(mark)
    if(int(mark) >= 50):
        print("pass")
    elif(int(mark) <50 and int(mark) >= 30):
        print('need to study')
    else:
        print("fail")
    mark = input('enter a number:\n')

print('end program')

# infinite loop
while (num < 10): #ture
    print('hello')
#print hello looping