# Sample code for class declaration of bundles for RPI Bakeoff Negotiation

# This is a multiplicative constant that will be used to determine our starting price.
# Right now, it is set to 'x' times the unit cost
UNIT_TO_SELLING = 3

class Bundle:

    def __init__(self, egg_cost, egg_unit, egg_quantity=0,\
    flour_cost, flour_unit, flour_quantity=0,\
    milk_cost, milk_unit, milk_quantity=0,\
    sugar_cost, sugar_unit, sugar_quantity=0,\
    bakingpowder_cost, bakingpowder_unit, bakingpowder_quantity=0,\
    chocolate_cost, chocolate_unit, chocolate_quantity=0,\
    vanilla_cost, vanilla_unit, vanilla_quantity=0,\
    blueberry_cost, blueberry_unit, blueberry_quantity=0):

        self.bundle =
        {
            "Eggs" : Eggs(egg_cost*UNIT_TO_SELLING, egg_cost, egg_unit, egg_quantity),
            "Flour" : Flour(flour_cost*UNIT_TO_SELLING, flour_cost, flour_unit, flour_quantity),
            "Milk" : Milk(milk_cost*UNIT_TO_SELLING, milk_cost, milk_unit, milk_quantity),
            "Sugar" : Sugar(sugar_cost*UNIT_TO_SELLING, sugar_cost, sugar_unit, sugar_quantity),
            "Baking Powder" : BakingPowder(bakingpowder_cost*UNIT_TO_SELLING, bakingpowder_cost, bakingpowder_unit, bakingpowder_quantity),
            "Chocolate Flavor" : ChocolateFlavor(chocolate_cost*UNIT_TO_SELLING, chocolate_cost, chocolate_unit, chocolate_quantity),
            "Vanilla Flavor" : VanillaFlavor(vanilla_cost*UNIT_TO_SELLING, vanilla_cost, vanilla_unit, vanilla_quantity),
            "Blueberry Flavor" : BlueberryFlavor(blueberry_cost*UNIT_TO_SELLING, blueberry_cost, blueberry_unit, blueberry_quantity)
        }

        self.total_price = 0

    def calculate_total_price():
        self.total_price = 0
        for item in self.bundle:
            self.total_price += self.bundle[item].price * self.bundle[item].quantity

    def is_profitable():
        total_unit_price = 0
        for item in self.bundle:
            total_unit_price += self.bundle[item].min_price * self.bundle[item].quantity
        calculate_total_price()
        return self.total_price > total_unit_price

    def to_string():
        string = "The current offer is "
        for item in self.bundle:
            if self.bundle[item].quantity > 0:
                string += str(self.bundle[item].quantity))
                string += " "
                if (item != "Eggs"):
                    string += self.bundle[item].unit
                    string += " of "
                string += item
                string += ","
        string += " for $"
        string += str(calculate_total_price)
        return string


class Item():
    def __init__(self, starting_price, unit_price, unit, quantity):
        self.price = starting_price
        self.unit_price = unit_price
        self.quantity = quantity # default set to 0
        self.unit = unit # example: "cups", "each", "packets"

    def can_reduce_price():
        return self.price > self.unit_price

    def reduce_price():
        if can_reduce_price:
            # reduce the current price by 20% if it does not go below our minimum unit cost
            self.price *= 0.80
        else:
            # this is the lowest we can go without losing profit
            self.price = self.unit_price

    def set_price(new_price):
        self.price = new_price

    # increase the number if items we are selling to a new amount
    # if an arguement is not provided, simply increase the current quantity by 1
    def set_quantity(new_quantity):
        self.quantity = new_quantity


class Eggs(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(self, starting_price, unit_price, unit, quantity)

class Flour(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(self, starting_price, unit_price, unit, quantity)

class Milk(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(self, starting_price, unit_price, unit, quantity)

class Sugar(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(self, starting_price, unit_price, unit, quantity)

class BakingPowder(Item):
        def __init__(self, starting_price, unit_price, unit, quantity):
            super().__init__(self, starting_price, unit_price, unit, quantity)

class ChocolateFlavor(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(self, starting_price, unit_price, unit, quantity)

class VanillaFlavor(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(self, starting_price, unit_price, unit, quantity)

class BlueberryFlavor(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(self, starting_price, unit_price, unit, quantity)
