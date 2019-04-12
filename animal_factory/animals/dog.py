from animal_factory.animals import Animal


class Dog(Animal):
    name = "Dog"

    def __init__(self):
        super(self.__class__, self).__init__()


if __name__ == "__main__":
    dog = Dog()
    dog.sleep()
    dog.eat()
    dog.breath()
