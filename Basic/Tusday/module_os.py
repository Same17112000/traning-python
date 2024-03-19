"""
 module os allow us to easily navigate files and directories 
 on the computer and then perform actions on them, such as moving them
 or deleting them
 """

import os
import shutil

print(os.getcwd())
print(os.listdir())

f = open('practice.txt', 'w+')
f.write("This is a test string")
f.close()

shutil.move("practice.txt","d:\\PYTHON\\training-python\\Basic\\Tusday")
