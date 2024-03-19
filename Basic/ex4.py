"""
 so sanh chu cai dau tien cua str nhap vao 
"""

mystring = input()
def myfunc(mystring):
    word_list = mystring.split()
    return word_list[0][0] == word_list[1][0]
        
a = myfunc(mystring)
print(a)