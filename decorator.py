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

    description = 'Dark Roast'
    price = 0.99

    def cost(self):
        return self.price

    def get_description(self):
        return self.description


class CondimentDecorator(Beverage):
    """Base decorator."""

    _component = None
    description = None

    def __init__(self, component: Beverage):
        self.component = component

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, value: Beverage):
        self._component = value

    def cost(self):
        return self.component.cost()

    def get_description(self):
        return f'{self.component.get_description()} + {self.description}'


class Whip(CondimentDecorator):
    """Concrete decorator."""

    description = 'Whip'
    price = 0.1

    def cost(self):
        return self.price + self.component.cost()


class Mocha(CondimentDecorator):
    """Concrete decorator."""

    description = 'Chocolate Mocha'
    price = 0.2

    def cost(self):
        return self.price + self.component.cost()


if __name__ == '__main__':
    bvg = DarkRoast()
    cafe = Whip(Mocha(bvg))
    print(cafe.get_description())
    print(cafe.cost())
