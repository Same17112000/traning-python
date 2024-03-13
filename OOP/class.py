class Car:
     # class attribute
     typecar = "mini car"

     # Instance attribute
     def __init__(self, para_namecar,para_color, para_material):
        self.namecar = para_namecar
        self.color = para_color
        self.material = para_material

# instantiate the Car class
toyota = Car("Toyota", "Red", "Electric")
porsche = Car("porsche", "yellow", "Deisel")
Honda = Car("Honda", "Blue", "Gas")
 
# access the class attributes
print("Honda is: ",Car.typecar)
print("Toyota is {}.".format(toyota.__class__.typecar))
print("porsche also is {}.".format(porsche.__class__.typecar))

# access the instance attributes
print("car {}'s color {}. {} is the operating material.".format( toyota.namecar, toyota.color, toyota.material))
print("car {}'s color {}. {} is the operating material.".format( porsche.namecar, porsche.color,porsche.material))
print("car {}'s color {}. {} is the operating material.".format( Honda.namecar, Honda.color, Honda.material))