class Insect:

    number_of_legs = 6

    def __init__(self,name=None,speed=None,mass=None,population=None,habitat=None,legs=None):
        self.__name = name
        self.__speed = speed
        self.__mass = mass
        self.population = population
        self.habitat = habitat
        self.legs = legs if legs is not None else Insect.number_of_legs

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
        return (
            f"Insect:\n"
            f"  Name: {self.__name}\n"
            f"  Speed: {self.__speed} m/s\n"
            f"  Mass: {self.__mass} g\n"
            f"  Legs: {self.legs}\n"
            f"  Population: {self.population}\n"
            f"  Habitat: {self.habitat}"
        )

    def __repr__(self):
        return (
            f"Insect(name={self.__name}, speed={self.__speed}, mass={self.__mass}, "
            f"legs={self.legs}, population={self.population}, habitat={self.habitat})"
        )
    
    def __del__(self):
        print(f"Object '{self.__name}' was deleted")

def main():
    insect_1 = Insect("Bee", 5.5, 0.1, 1500, "Tropics")
    insect_2 = Insect("Butterfly", 2.0, 0.3, 2000, "Forest")
    insect_3 = Insect("Ant", 0.02, 0.002, 2500, "Anywhere")
    insect_4 = Insect()
    insect_5 = Insect("Insect 5", 1, 1, 1, "Habitat 5", 10)

    print(insect_1)
    print(insect_2)
    print(insect_3)
    print(insect_4)
    print(Insect.number_of_legs)
    print(insect_5)
    print(insect_5.legs)

main()
