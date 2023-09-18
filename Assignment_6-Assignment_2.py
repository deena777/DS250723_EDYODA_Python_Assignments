'''
1. Create a class named ‘Dog’.  
   It should have a constructor which accepts its name, age and coat color. You must perform the following operations:
   🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
   🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
   🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. 
         It should have at least two methods of its own.
   🔴 d. Create objects and implement the above functionalities.

'''



class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, special_skill):
        super().__init__(name, age, coat_color)
        self.special_skill = special_skill

    def describe_skill(self):
        print(f"{self.name} has a special skill: {self.special_skill}")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def describe_weight(self):
        print(f"{self.name} weighs {self.weight} pounds.")



dog1 = Dog("Buddy", 3, "Brown")
dog1.description()
dog1.get_info()


jack = JackRussellTerrier("Rusty", 2, "White", "Jumping high")
jack.description()
jack.get_info()
jack.describe_skill()


bull = Bulldog("Max", 4, "Black", 70)
bull.description()
bull.get_info()
bull.describe_weight()
