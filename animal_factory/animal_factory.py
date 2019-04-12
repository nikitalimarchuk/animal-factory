import animals
import inspect

from animals.animal import Animal


class Animalfactory(object):
    def __init__(self):
        self.target_animal = Animal
        self.animals_pool = [Animal]

    def get_target_animal(self, animal_name):
        """Method factory for getting needed animal class from

        :param animal_name: name of animal in string
        :return: <class> object"""

        for key, value in animals.__dict__.items():
            if inspect.isclass(value):
                if issubclass(value, Animal):
                    if value.name == animal_name:
                        self.target_animal = value
                        self.animals_pool.append(value)
                        break
        else:
            raise Exception("No animal with name {} was found in pool.".format(animal_name))


if __name__ == "__main__":
    animal_factory = Animalfactory()
    animal_factory.get_target_animal("Cat")
    animal = animal_factory.target_animal()
    animal.sleep()
    animal.eat()
    animal.breath()
