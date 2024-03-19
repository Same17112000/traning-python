class Car:
    def __init__(self, para_namecar, para_color):
        self.namecar = para_namecar
        self.color = para_color
    
    def name(self):
        return "The name of car is " + self.namecar
    
    @classmethod
    def from_string(cls, s):
        lst = s.split("-")
        new_lst = [st.strip() for st in lst]
        namecar, color = new_lst
        return cls(namecar, color)

# toyota = Car("Toyota", "red")
infor_str = "Toyota - red"
toyota = Car.from_string(infor_str)

print(toyota.name())
print(Car.name(toyota))

print(toyota.__dict__)

# ////////////reverse string//////////////////////
# def reverse(input_str):
#     str = input_str.split(" ")
#     rever_str = str[::-1]
#     reversed_str = ":".join(rever_str)
#     return reversed_str

# str = "ab,cd,ef,gh"
# result = reverse(str)
# print(result)


