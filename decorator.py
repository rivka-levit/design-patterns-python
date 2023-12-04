from abc import ABC, abstractmethod


class Beverage(ABC):
    """Abstract component."""

    description = None
    price = None

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class DarkRoast(Beverage):
    """Concrete component."""

    description = 'Dark Roast Coffee'
    price = 0.99

    def cost(self):
        return self.price

    def get_description(self):
        return self.description


class HouseBlend(Beverage):
    """Concrete component"""

    description = 'House Blend Coffee'
    price = 0.89

    def cost(self):
        return self.price

    def get_description(self):
        return self.description


class CondimentDecorator(Beverage):
    """Base decorator."""

    _component = None

    def __init__(self, component: Beverage):
        self.component = component

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, value: Beverage):
        self._component = value

    def cost(self):
        return self.price + self.component.cost()

    def get_description(self):
        return f'{self.component.get_description()}, {self.description}'


class Whip(CondimentDecorator):
    """Concrete decorator."""

    description = 'Whip'
    price = 0.1


class Mocha(CondimentDecorator):
    """Concrete decorator."""

    description = 'Mocha'
    price = 0.15


class Soy(CondimentDecorator):
    """Concrete decorator"""

    description = 'Soy'
    price = 0.2


if __name__ == '__main__':
    cafe = Whip(Mocha(DarkRoast()))
    print(f'{cafe.get_description()} -- ${cafe.cost()}')

    cafe = Whip(Mocha(Mocha(Soy(HouseBlend()))))
    print(f'{cafe.get_description()} -- ${cafe.cost()}')
