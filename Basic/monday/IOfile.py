import os 

f = open("python_ioFile.txt")
contents = f.readline()
print(contents)  

with open('python_ioFile.txt', mode='r') as f:
    print(f.read())
    
with open('python_ioFile.txt', mode='a') as f:
    f.write('Hello too')

with open('python_ioFile.txt', mode='r') as f:
    print(f.read())