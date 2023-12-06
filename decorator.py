from abc import ABC, abstractmethod


class Beverage(ABC):
    """Abstract component."""

    description = None
    price_s = None
    price_m = None
    price_l = None
    size = None
    list_sizes = {'s': 'Small', 'm': 'Medium', 'l': 'Large'}

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def set_size(self, size: str):
        pass

    @abstractmethod
    def get_size(self):
        pass


class DarkRoast(Beverage):
    """Concrete component."""

    description = 'Dark Roast Coffee'
    price_s = 0.99
    price_m = 1.05
    price_l = 1.15

    def __init__(self, size: str):
        self.set_size(size)

    def cost(self):
        if self.size == 's':
            return self.price_s
        if self.size == 'm':
            return self.price_m
        return self.price_l

    def get_description(self):
        return f'{self.description} {self.list_sizes[self.size]}'

    def get_size(self):
        return self.size

    def set_size(self, size: str):
        if size in self.list_sizes:
            self.size = size
        else:
            raise AttributeError('Size must be one of values: s, m, l')


class HouseBlend(Beverage):
    """Concrete component"""

    description = 'House Blend Coffee'
    price_s = 0.89
    price_m = 0.99
    price_l = 1.09

    def __init__(self, size: str):
        self.set_size(size)

    def cost(self):
        if self.size == 's':
            return self.price_s
        if self.size == 'm':
            return self.price_m
        return self.price_l

    def get_description(self):
        return f'{self.description} {self.list_sizes[self.size]}'

    def get_size(self):
        return self.size

    def set_size(self, size: str):
        if size in self.list_sizes:
            self.size = size
        else:
            raise AttributeError('Size must be one of values: s, m, l')


class CondimentDecorator(Beverage):
    """Base decorator."""

    _component = None

    def __init__(self, component: Beverage):
        self.component = component
        self.size = self.component.get_size()

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, value: Beverage):
        self._component = value

    def cost(self):
        if self.size == 's':
            return self.price_s + self.component.cost()
        if self.size == 'm':
            return self.price_m + self.component.cost()
        return self.price_l + self.component.cost()

    def get_description(self):
        return f'{self.component.get_description()}, {self.description}'

    def get_size(self):
        return self.size

    def set_size(self, size: str):
        if size in self.list_sizes:
            self.size = size
        else:
            raise AttributeError('Size must be one of values: s, m, l')


class Whip(CondimentDecorator):
    """Concrete decorator."""

    description = 'Whip'
    price_s = 0.1
    price_m = 0.15
    price_l = 0.2


class Mocha(CondimentDecorator):
    """Concrete decorator."""

    description = 'Mocha'
    price_s = 0.15
    price_m = 0.2
    price_l = 0.25


class Soy(CondimentDecorator):
    """Concrete decorator"""

    description = 'Soy'
    price_s = 0.2
    price_m = 0.25
    price_l = 0.3


if __name__ == '__main__':
    cafe = Whip(Mocha(DarkRoast('l')))
    print(f'{cafe.get_description()} -- ${cafe.cost()}')

    cafe = Whip(Mocha(Mocha(Soy(HouseBlend('s')))))
    print(f'{cafe.get_description()} -- ${cafe.cost()}')
