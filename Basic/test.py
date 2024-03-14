str = "Learn how to use the  yield keyword to     create and iterate over generators"

str1 = str.split()
print(len(str1))
print(str1)

prev = ""
count = 0
for i in str:
    if i == " " and i != prev:
        count += 1
    prev = i

print(count)


str = str.split()
print(len(str) -1 )






# for i in range(str.len()):

    
