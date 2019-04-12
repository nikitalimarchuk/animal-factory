from animals.animal import Animal


class Monkey(Animal):
    name = "Monkey"

    def __init__(self):
        super(self.__class__, self).__init__()


if __name__ == "__main__":
    monkey = Monkey()
    monkey.sleep()
    monkey.eat()
    monkey.breath()
