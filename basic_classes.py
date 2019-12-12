# Sample code for class declaration of bundles for RPI Bakeoff Negotiation

# This is a multiplicative constant that will be used to determine our starting price.
# Right now, it is set to 'x' times the unit cost
UNIT_TO_SELLING = 3

class Bundle:

    def __init__(self, egg_cost, flour_cost, milk_cost, sugar_cost, chocolate_cost, vanilla_cost, blueberry_cost,\
    egg_unit, flour_unit, milk_unit, sugar_unit, chocolate_unit, vanilla_unit, blueberry_unit,\
    egg_quantity=-1, flour_quantity=-1, milk_quantity=-1, sugar_quantity=-1, chocolate_quantity=-1, vanilla_quantity=-1, blueberry_quantity=-1):

        self.bundle = {
            "egg" : Eggs(egg_cost*UNIT_TO_SELLING, egg_cost, egg_unit, egg_quantity),
            "flour" : Flour(flour_cost*UNIT_TO_SELLING, flour_cost, flour_unit, flour_quantity),
            "milk" : Milk(milk_cost*UNIT_TO_SELLING, milk_cost, milk_unit, milk_quantity),
            "sugar" : Sugar(sugar_cost*UNIT_TO_SELLING, sugar_cost, sugar_unit, sugar_quantity),
            "chocolate" : ChocolateFlavor(chocolate_cost*UNIT_TO_SELLING, chocolate_cost, chocolate_unit, chocolate_quantity),
            "vanilla" : VanillaFlavor(vanilla_cost*UNIT_TO_SELLING, vanilla_cost, vanilla_unit, vanilla_quantity),
            "blueberry" : BlueberryFlavor(blueberry_cost*UNIT_TO_SELLING, blueberry_cost, blueberry_unit, blueberry_quantity)
        }

        # calculate the minimum price of the bundle based on each items' unit cost and the current cost
        self.total_unit_price = 0
        self.current_price = 0


    def update_unit_price(self):
        self.total_unit_price = 0
        for item in self.bundle:
            if self.bundle[item].quantity != -1:
                self.total_unit_price += self.bundle[item].unit_price * self.bundle[item].quantity
        print("UNIT PRICE", self.total_unit_price)


    # unit price * quantity
    # current price * quantity
    def update_current_price(self):
        self.update_unit_price()
        self.current_price = self.total_unit_price * UNIT_TO_SELLING
        # for item in self.bundle:
        #     self.current_price += self.bundle[item].price * self.bundle[item].quantity


    def update_current_price_diff(self,difference ):
        for item in difference:
            self.current_price -= difference[item] * self.bundle[item].unit_price*UNIT_TO_SELLING

    def update_quantity(self,products):
        difference = {"egg": 0, "flour": 0, "sugar": 0, "milk": 0, "chocolate": 0, "blueberry": 0, "vanilla": 0}
        # 'products' is a dictionary that would already be updated in parse_sentence.py
        for item in products:
            if products[item] != -1:
                difference[item] = self.bundle[item].quantity - products[item]
                self.bundle[item].quantity = products[item]
        self.update_unit_price()
        self.update_current_price_diff(difference)


    def set_price(self,new_price):
        self.current_price = new_price

    def is_profitable(self):
        return self.current_price > self.total_unit_price

    def reduce_price(self):
        if self.is_profitable():
            self.current_price =max(self.current_price * 0.80 , self.total_unit_price)


    def clear_bundle(self):
        self.current_price = 0
        for item in self.bundle:
            self.bundle[item].quantity = 0

    def to_string(self):
        string = "I can offer you "
        for item in self.bundle:
            if self.bundle[item].quantity > 0:
                string += str(self.bundle[item].quantity)
                string += " "
                if (item != "egg"):
                    string += self.bundle[item].unit
                    string += " of "
                string += item
                if(item == "egg" and self.bundle[item].quantity>1):
                    string += "s"
                string += ", "
        string += "for $"
        string += str(round(self.current_price,2))
        return string


class Item:
    def __init__(self, starting_price, unit_price, unit, quantity):
        self.price = starting_price
        self.unit_price = unit_price
        self.quantity = quantity # default set to 0
        self.unit = unit # example: "cups", "each", "packets"

    def can_reduce_price():
        return self.price > self.unit_price


    def set_price(new_price):
        self.price = new_price

    # increase the number if items we are selling to a new amount
    # if an arguement is not provided, simply increase the current quantity by 1
    def set_quantity(new_quantity):
        self.quantity = new_quantity


class Eggs(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(starting_price, unit_price, unit, quantity)

class Flour(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(starting_price, unit_price, unit, quantity)

class Milk(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(starting_price, unit_price, unit, quantity)

class Sugar(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(starting_price, unit_price, unit, quantity)

class BakingPowder(Item):
        def __init__(self, starting_price, unit_price, unit, quantity):
            super().__init__(starting_price, unit_price, unit, quantity)

class ChocolateFlavor(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(starting_price, unit_price, unit, quantity)

class VanillaFlavor(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(starting_price, unit_price, unit, quantity)

class BlueberryFlavor(Item):
    def __init__(self, starting_price, unit_price, unit, quantity):
        super().__init__(starting_price, unit_price, unit, quantity)
