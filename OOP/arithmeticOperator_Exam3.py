"""
    Create a calculate class.
    Include methods for basic arthimetic operation
"""

class Calculate:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x + self.y
    
    def substract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y

    def devide(self):
        if self.y != 0:
            return self.x /self.y
        else:
            print("Can not devide")

cal = Calculate(3,6)    

print("add:",cal.add())

