# Sample code for class declaration of bundles for RPI Bakeoff Negotiation

# This is a multiplicative constant that will be used to determine our starting price.
# Right now, it is set to 5 times the unit cost
UNIT_TO_SELLING = 5

class Bundle:

    def __init__(self, egg_cost, egg_unit, flour_cost, flour_unit, milk_cost, milk_unit, sugar_cost, sugar_unit, \
    bakingpowder_cost, bakingpowder_unit, chocolate_cost, chocolate_unit, vanilla_cost, vanilla_unit, blueberry_cost, blueberry_unit):

        self.bundle =
        {
            "Eggs" : Eggs(egg_cost*UNIT_TO_SELLING, egg_cost, egg_unit),
            "Flour" : Flour(flour_cost*UNIT_TO_SELLING, flour_cost, flour_unit),
            "Milk" : Milk(milk_cost*UNIT_TO_SELLING, milk_cost, milk_unit),
            "Sugar" : Sugar(sugar_cost*UNIT_TO_SELLING, sugar_cost, sugar_unit),
            "Baking Powder" : BakingPowder(bakingpowder_cost*UNIT_TO_SELLING, bakingpowder_cost, bakingpowder_unit),
            "Chocolate Flavor" : ChocolateFlavor(chocolate_cost*UNIT_TO_SELLING, chocolate_cost, chocolate_unit),
            "Vanilla Flavor" : VanillaFlavor(vanilla_cost*UNIT_TO_SELLING, vanilla_cost, vanilla_unit),
            "Blueberry Flavor" : BlueberryFlavor(blueberry_cost*UNIT_TO_SELLING, blueberry_cost, blueberry_unit)
        }

        self.total_price = 0

    def calculate_total_price():
        self.total_price = 0
        for item in self.bundle:
            self.total_price += self.bundle[item].price * self.bundle[item].quantity

    def toString():
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
    def __init__(self, starting_price, min_price, unit):
        self.price = starting_price
        self.min_price = min_price
        self.quantity = 0
        self.unit = unit # example: "cups", "each", "packets"

    def can_reduce_price():
        return self.price > self.min_price

    def reduce_price():
        if can_reduce_price:
            # reduce the current price by 20% if it does not go below our minimum unit cost
            self.price *= 0.80
        else:
            # this is the lowest we can go without losing profit
            self.price = self.min_price

    # increase the number if items we are selling to a new amount
    # if an arguement is not provided, simply increase the current quantity by 1
    def increase_quantity(new_quantity=self.quantity+1):
        self.quantity = new_quantity


class Eggs(Item):
    def __init__(self, starting_price, min_price):
        super().__init__(self, starting_price, min_price)

class Flour(Item):
    def __init__(self, starting_price, min_price):
        super().__init__(self, starting_price, min_price)

class Milk(Item):
    def __init__(self, starting_price, min_price):
        super().__init__(self, starting_price, min_price)

class Sugar(Item):
    def __init__(self, starting_price, min_price):
        super().__init__(self, starting_price, min_price)

class BakingPowder(Item):
        def __init__(self, starting_price, min_price):
            super().__init__(self, starting_price, min_price)

class ChocolateFlavor(Item):
    def __init__(self, starting_price, min_price):
        super().__init__(self, starting_price, min_price)

class VanillaFlavor(Item):
    def __init__(self, starting_price, min_price):
        super().__init__(self, starting_price, min_price)

class BlueberryFlavor(Item):
    def __init__(self, starting_price, min_price):
        super().__init__(self, starting_price, min_price)
