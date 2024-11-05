class Insect:

    legs = 6

    def __init__(self, name = None, speed = None, mass = None, population = None, habitat = None, legs= None):
        self.__name = name
        self.__speed = speed
        self.__mass = mass
        self.population = population
        self.habitat = habitat
        self.legs = legs

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        self.__speed = speed

    def get_mass(self):
        return self.__mass
    
    def set_mass(self, mass):
        self.__mass = mass

    def __str__(self):
        return f"Insect: {self.__name}, {self.__speed} m/s, {self.__mass} g, {self.legs} Population: {self.population}, Habitat: {self.habitat}"

    def __repr__(self):
        return f"Insect(name={self.__name}, speed={self.__speed}, mass={self.__mass}, legs = {self.legs}, population = {self.population}, habitat = {self.habitat})"
    
    def __del__(self):
        print(f"Object '{self.__name}' was deleted")

def main():
    insect1 = Insect("Bee", 5.5, 0.1, 1500, "Tropics")
    insect2 = Insect("Butterfly", 2.0, 0.3, 2000, "Forest")
    insect3 = Insect("Ant", 0.02, 0.002, 2500, "Anywhere")
    insect4 = Insect()
    insect5 = Insect("1", 1, 1, 1, "1", 10)

    print(insect1)
    print(insect2)
    print(insect3)
    print(insect4)
    print(Insect.legs)
    print(insect5)
    print(insect5.legs)

main()
