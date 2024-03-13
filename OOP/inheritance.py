# class Idol:
#     def __init__(self, name, age, appearence):
#         self.name = name
#         self.age = age
#         self.__appearance = appearence

#     def getAppearence(self):
#         return self.__appearance
#     def setAppearence(self, value):
#         self.__appearence = value

#     def liveStream(self):
#         pass

# class KhaBanh(Idol):
#     def __init__(self, name, age, appearence, location):
#         super().__init__(name, age, appearence)
#         self.location = location

#     def signatureQuote(self):
#         print("Ao that day!")

# class TienBip(Idol):
#     def signatureQuote(self):
#         print("Con cai nit!")

# kb = KhaBanh("Kha", 30, "dau moi", "trong tu")
# print(kb.name)
# print(kb.location)

# kb.setAppearence("longHair")
# print(kb.getAppearence())
# kb.signatureQuote()

# tb = TienBip("Tien", 40, "troc")
# print(tb.name)
# tb.signatureQuote()

#################################################################
# Python code to demonstrate how parent constructors
# are called.
 
# parent class
class Person:
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
     
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
 
 
# creation of an object variable or an instance
a = Employee('Bang', 886012, 200000, "Intern")
 
# calling a function of the class Person using
# its instance
a.display()
a.details()