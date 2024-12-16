#created myModule.py

import myModule
print(myModule.teacher)
myModule.sayHello()

from myModule import sayHello, teacher
sayHello()
print(teacher)

from myModule import * #import all everything
sayHello()
print(teacher)

#built in module offically
#ex Math, datetime, OS

import os
print(os.getcwd()) #root path

"""os.mkdir('myproject')"""

import random
print(random.random())