from animal_factory.animals import Animal


class Bear(Animal):
    name = "Bear"

    def __init__(self):
        super(self.__class__, self).__init__()


if __name__ == "__main__":
    bear = Bear()
    bear.sleep()
    bear.eat()
    bear.breath()
