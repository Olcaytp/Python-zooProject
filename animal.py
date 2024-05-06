class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100

    def eat(self, food):
        pass

    def sleep(self):
        pass

    def make_sound(self):
        pass


class Herbivore(Animal):
    def eat(self, food):
        if food == 'grass':
            self.energy += 20
        else:
            print(f"{self.name} doesn't eat {food}!")
        self.adjust_energy()

    def play(self, other_animal):
        if self.energy <= 0 or other_animal.energy <= 0:
            print(f"{self.name} doesn't have enough energy to play.")
            return
        
        elif isinstance(other_animal, Herbivore):
            print(f"{self.name} is playing with {other_animal.name}!")
            self.energy -= 20
            other_animal.energy -= 20
        else:
            print(f"{self.name} can only play with other herbivores!")
        #self.adjust_energy()
        print('--------------------------------')

    def adjust_energy(self):
        if self.energy < 0:
            self.energy = 0
        elif self.energy > 100:
            self.energy = 100


class Carnivore(Animal):
    def eat(self, food):
        if food == 'meat':
            self.energy += 30
        else:
            print(f"{self.name} doesn't eat {food}!")
        self.adjust_energy()

    def hunt(self, other_animal):
        if other_animal.energy > 0:
            print(f"{self.name} is hunting {other_animal.name}!")
            other_animal.energy -= 50
            self.energy += 50
            #self.adjust_energy()
            print(f"{self.name}'s energy level: {self.energy}")
            print(f"{other_animal.name}'s energy level: {other_animal.energy}")
        else:
            print(f"{other_animal.name} has no energy left.{self.name} Can't hunt it.")
        print('--------------------------------')
    def play(self, other_animal):
        if isinstance(other_animal, Carnivore):
            print(f"{self.name} is playing with {other_animal.name}!")
            self.energy -= 20
            other_animal.energy -= 20
        else:
            print(f"{self.name} can only play with other carnivores!")
        self.adjust_energy()
        print('--------------------------------')

    def adjust_energy(self):
        if self.energy < 0:
            self.energy = 0
        elif self.energy > 100:
            self.energy = 100


class Lion(Carnivore):
    def make_sound(self):
        return "Roar!"

class Leopard(Carnivore):
    def make_sound(self):
        return "Meow!"

class Elephant(Herbivore):
    def make_sound(self):
        return "Trumpet!"

class Giraffe(Herbivore):
    def make_sound(self):
        return "Moo!"
