str = "Learn how to use the  yield keyword to     create and iterate over generators"

prev = ""
count = 0
for i in str:
    if i == " " and i != prev:
        count += 1
    prev = i

print(count)

# str = "Learn how to use the  yield keyword to     create and iterate over generators"
# str1 = str.split()
# print(len(str1) - 1)



# str = "Learn how to use the  yield keyword to     create and iterate over generators"
# count = 0
# for i in str:
#     if i == " ":
#         count += 1

# print(count)

    
