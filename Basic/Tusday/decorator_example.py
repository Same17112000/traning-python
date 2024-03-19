#////////////////////ex1/////////////////////////

# def hello(name = 'Bang'):
#     print('The hello() function has been executed')

#     def welcome():
#         return '\t This is welcome() function inside hello'
    
#     print("I am going to return a function")

#     if name == "Bang":
#         return welcome
#     else:
#         pass

# my_new_func = hello('Bang')

# print(my_new_func())

# /////////////////ex2///////////////////////////

# def cool():
#     def super_cool():
#         return "I am very cool"
    
#     return super_cool

# some_func = cool()
# print(some_func())


# //////////////////ex3///////////////////////////

# def hello():
#     return 'Hi Bang'

# def other(some_def_func):
#     print('Other code runs here')
#     print(some_def_func)

# print(other(hello))



# ///////////////////ex4///////////////////////////

# def new_decorator(original_func):
#     def wrap_func():
#         print("Some extra code, before the original function")

#         original_func()
#         print("Some extra code, after the original function ")

#     return wrap_func

# @new_decorator
# def func_needs_decorator():
#     print("I want to be decorator")

# print(func_needs_decorator())

# ****/////////////////ex5/////////////////////////////////////
# class decoclass(object):
#     def __init__(self, f):
#         self.f = f
#     def __call__(self, *args, **kwargs):
#         # logic trước khi gọi hàm f
#         print('decorator initialised')
#         self.f(*args, **kwargs)
#         print('decorator terminated')
#         # logic sau khi gọi hàm f

# @decoclass
# def hello(name):
#     print(f'Hello, {name}. Welcome to heaven!')

# hello('Obama')


# truyen tham so
def run_time(num):
    def test(func):
        for i in range(0,num):
            func()
    
    return test

# truyen tham so ham se tu chay ko can goi lai ham say_Hello
@run_time(5) 
def say_Hello():
    print("Hello")



