import random
from animal import Herbivore, Carnivore
from animal import Lion, Elephant, Giraffe, Leopard

class Zoo:
    def __init__(self):
        self.animals = []
        self.visitors = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_visitor(self, visitor):
        self.visitors.append(visitor)

    def feed_animal(self, animal, food_type):
        animal.eat(food_type)

    def feed_specific_animal(self):
        print("Which animal would you like to feed?")
        for index, animal in enumerate(self.animals):
            print(f"{index + 1}. {animal.name}")

        choice = input("Enter the number of the animal you want to feed: ")

        try:
            choice_index = int(choice) - 1
            chosen_animal = self.animals[choice_index]
            
            if isinstance(chosen_animal, Herbivore):
                food_type = 'grass'
            else:
                food_type = 'meat'
            
            self.feed_animal(chosen_animal, food_type)
            print(f"{chosen_animal.name} is eating {food_type}. Energy level: {chosen_animal.energy}")

        except (ValueError, IndexError):
            print("Invalid choice. No animal is fed.")

    def choose_activity(self):
        print("Which activity would you like to perform?")
        print("1. Feed animals")
        print("2. Rest animals")
        print("3. Interactions between animals")
        choice = input("Enter your choice: ")
        print('--------------------------------')

        if choice == "1":
            self.feed_specific_animal()
        elif choice == "2":
            self.rest_animals()
        elif choice == "3":
            self.interact_between_animals()
        else:
            print("Invalid choice. Please enter a valid option.")

    def rest_animals(self):
        for animal in self.animals:
            animal.sleep()
            print(f"{animal.name} is resting. Energy level: {animal.energy}")
        print('--------------------------------')

    def interact_between_animals(self):
        for animal in self.animals:
            if isinstance(animal, Carnivore):
                 prey_options = [other_animal for other_animal in self.animals if isinstance(other_animal, Herbivore)]
                 if prey_options:
                    prey = random.choice(prey_options)
                    animal.hunt(prey)
                    animal.adjust_energy()
                    prey.adjust_energy()
            elif isinstance(animal, Herbivore):
                partner_options = [other_animal for other_animal in self.animals if isinstance(other_animal, Herbivore) and other_animal != animal]
                if partner_options:
                    partner = random.choice(partner_options)
                    animal.play(partner)
                    animal.adjust_energy()
                    partner.adjust_energy()

    def simulate_day(self):
        print("Simulating a day in the zoo...\n")

        while True:
            # Ask user which activity they want to perform
            self.choose_activity()

            # Make sounds
            for animal in self.animals:
                print(f"{animal.name} says: {animal.make_sound()}")

            print('--------------------------------')
            # Visitors enjoy their visit to the zoo!
            for visitor in self.visitors:
                print(f"{visitor.name} enjoyed their visit to the zoo!")

            # Ask user if they want to continue simulating
            while True:
                continue_simulation_input = input("Continue simulating? (yes/no): ").lower().strip()

                if continue_simulation_input == "no" or continue_simulation_input == "n":
                    print("Exiting simulation...")
                    return
                elif continue_simulation_input == "yes" or continue_simulation_input == "y":
                    print('Continue simulating!')
                    break
                else:
                    print('Invalid option. Please enter a valid option.')

# Example usage:

if __name__ == "__main__":
    zoo = Zoo()

    lion = Lion("Leon", 5)
    elephant = Elephant("Elefo", 10)
    giraffe = Giraffe("Geoffrey", 7)
    leopard = Leopard("Leopard", 10)

    zoo.add_animal(lion)
    zoo.add_animal(leopard)
    zoo.add_animal(elephant)
    zoo.add_animal(giraffe)

    class Visitor:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    visitor1 = Visitor("Alice", 25)
    visitor2 = Visitor("Bob", 30)

    zoo.add_visitor(visitor1)
    zoo.add_visitor(visitor2)

    zoo.simulate_day()
