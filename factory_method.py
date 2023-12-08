from abc import ABC, abstractmethod


class Pizza(ABC):
    """Abstract product."""

    name: str = None
    dough: str = None
    sauce: str = None
    toppings = list()

    def prepare(self):
        print(f'Preparing {self.name}')
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings...')
        for topping in self.toppings:
            print('    ' + topping)

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')


class NYStyleCheesePizza(Pizza):
    """Concrete product."""

    name = 'NY Style Sauce and Cheese Pizza'
    dough = 'Thin Crust Dough'
    sauce = 'Marinara Sauce'
    toppings = ['Grated Reggiano Cheese']


class ChicagoCheesePizza(Pizza):
    """Concrete product."""

    name = 'Chicago Style Deep Dish Cheese Pizza'
    dough = 'Extra Thick Crust Dough'
    sauce = 'Plum Tomato Sauce'
    toppings = ['Shredded Mozzarella Cheese']

    def cut(self):
        print('Cutting the pizza into square slices')


class PizzaStore(ABC):
    """Abstract creator."""

    @abstractmethod
    def create_pizza(self, kind: str):
        """Abstract factory method"""
        pass

    def order_pizza(self, kind: str):
        pizza = self.create_pizza(kind)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    """Concrete creator."""

    def create_pizza(self, item):
        if item == 'cheese':
            return NYStyleCheesePizza()
        # elif item == 'veggie':
        #     return NYStyleVeggiePizza()
        # elif item == 'pepperoni':
        #     return NYStylePepperoniPizza()


class ChicagoPizzaStore(PizzaStore):
    """Concrete creator."""

    def create_pizza(self, item):
        if item == 'cheese':
            return ChicagoCheesePizza()
        # elif item == 'veggie':
        #     return ChicagoVeggiePizza()
        # elif item == 'pepperoni':
        #     return ChicagoPepperoniPizza()


if __name__ == '__main__':
    ny_store = NYPizzaStore()
    ch_store = ChicagoPizzaStore()
    pizza = ny_store.order_pizza('cheese')
    print(f'Ethan ordered a {pizza.name}\n')

    pizza = ch_store.order_pizza('cheese')
    print(f'Joel ordered a {pizza.name}')
