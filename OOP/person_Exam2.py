"""
    Create a person class.
    Include attributes like name, country, date of birth.
    Implement a method to determine the person's age
"""

from datetime import date

class person:
    def __init__(self, name, country, dateOfBirth):
        self.name = name
        self.country = country
        self.dateOfBirth = dateOfBirth
    
    def age(self):
        today = date.today()
        age = today.year - self.dateOfBirth.year
        if today < date(today.year, self.dateOfBirth.month, self.dateOfBirth.day):
            age -= 1
        return age
    
person1 = person("Bang","Viet Nam",date(2000,11,17))

print("Person1:")
print("Person1's name: ", person1.name)
print("Person1's country: ", person1.country)
print("Person1's date of birth: ", person1.dateOfBirth)
print("Person1's age: ", person1.age())