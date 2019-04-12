class Animal(object):
    name = ""

    def __init__(self):
        print "{} was born.".format(self.__class__.__name__)

    def breath(self):
        print "{} breathing...".format(self.__class__.__name__)

    def eat(self):
        print "{} eating...".format(self.__class__.__name__)

    def sleep(self):
        print "{} sleeping...".format(self.__class__.__name__)

    def __del__(self):
        print "{} was dead.".format(self.__class__.__name__)


if __name__ == "__main__":
    animal = Animal()
    animal.breath()
    animal.eat()
    animal.sleep()
