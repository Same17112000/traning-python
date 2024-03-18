

# print(list(range(0,11,2)))

# index_count = 0
# for i in 'abcde':
#     print('at index {} the letter is {}'.format(index_count,i))
#     index_count += 1


# index_count = 0
# word = 'abcde'
# for i in word:
#     print(word[index_count])
#     index_count += 1

# word = 'abcde'
# for i in enumerate(word):
#     print(i)

# print('\n')
# mylist1 = [1,2,3,4,5]
# mylist2 = ['a','b','c']
# mylist3 = [100,200,300]
# for i in zip(mylist1,mylist2,mylist3):
#     print(i)


# import random
# mylist = [1,2,3,4,5,6,7,8,9]
# random.shuffle(mylist)
# print(mylist)

# mystring = "Hello"
# mylist = []
# mylist = [i for i in mystring]
# print(mylist)

# results = [x if x % 2 == 0 else 'ODD' for x in range(0,11)]
# print(results)

# st = "My name is Bang"
# print(st.split())
# for word in st.split():
#     if word[1] == 'a':
#         print(word)

# st1 = 'Print every word in this sentence that has an even number of letters'
# for word in st1.split():
#     if len(word) % 2 == 0:
#         print(word + " is even!")

# st2 = 'Create a list of the first letters of every word in this string'
# newlist = [word[0] for word in st2.split()]
# newlist1 = "".join(newlist)
# print(newlist1)


num_list = [1,2,3,4,5,6,7,9,13]
even_list = []
def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass
    return even_list

check_even_list(num_list)
print(even_list)


