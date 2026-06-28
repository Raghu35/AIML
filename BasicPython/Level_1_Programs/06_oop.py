"""Level 1: Object-Oriented Programming concepts."""

class Animal:
    species = "Animal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    species = "Dog"

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks"

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


animal = Animal("Generic")
dog = Dog("Buddy", "Labrador")
account = BankAccount(100)
account.deposit(50)

print(animal.speak())
print(dog.speak())
print(dog)
print("Balance:", account.get_balance())
