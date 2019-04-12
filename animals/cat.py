from animals.animal import Animal


class Cat(Animal):
    name = "Cat"

    def __init__(self):
        super(self.__class__, self).__init__()


if __name__ == "__main__":
    cat = Cat()
    cat.sleep()
    cat.eat()
    cat.breath()
