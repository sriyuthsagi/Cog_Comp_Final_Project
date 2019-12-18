# Code for class declaration of bundles for RPI Bakeoff Negotiation

# This is a multiplicative constant that will be used to determine our starting price.
# Right now, it is set to 'x' times the unit cost
UNIT_TO_SELLING = 3

class Bundle:

    # This constructor is called when the agent sets Utilities in agent.py
    def __init__(self, egg_cost, flour_cost, milk_cost, sugar_cost, chocolate_cost, vanilla_cost, blueberry_cost,\
    egg_unit, flour_unit, milk_unit, sugar_unit, chocolate_unit, vanilla_unit, blueberry_unit,\
    egg_quantity=-1, flour_quantity=-1, milk_quantity=-1, sugar_quantity=-1, chocolate_quantity=-1, vanilla_quantity=-1, blueberry_quantity=-1):

        self.bundle = {
            # Note: The starting selling price of each item can be adjusted by changing the first parameter in each of these constructs.
            # Right now, they are set to 'UNIT_TO_SELLING' * the unit cost of each item
            "egg" : Eggs(egg_cost*UNIT_TO_SELLING, egg_cost, egg_unit, egg_quantity),
            "flour" : Flour(flour_cost*UNIT_TO_SELLING, flour_cost, flour_unit, flour_quantity),
            "milk" : Milk(milk_cost*UNIT_TO_SELLING, milk_cost, milk_unit, milk_quantity),
            "sugar" : Sugar(sugar_cost*UNIT_TO_SELLING, sugar_cost, sugar_unit, sugar_quantity),
            "chocolate" : ChocolateFlavor(chocolate_cost*UNIT_TO_SELLING, chocolate_cost, chocolate_unit, chocolate_quantity),
            "vanilla" : VanillaFlavor(vanilla_cost*UNIT_TO_SELLING, vanilla_cost, vanilla_unit, vanilla_quantity),
            "blueberry" : BlueberryFlavor(blueberry_cost*UNIT_TO_SELLING, blueberry_cost, blueberry_unit, blueberry_quantity)
        }

        # At construction, the quantity of every item in the bundle is 0, so price*quantity = 0
        self.total_unit_price = 0
        self.current_price = 0


    def update_unit_price(self):
        self.total_unit_price = 0
        for item in self.bundle:
            if self.bundle[item].quantity != -1:
                self.total_unit_price += self.bundle[item].unit_price * self.bundle[item].quantity
        # print("UNIT PRICE", self.total_unit_price)


    def update_current_price(self):
        self.update_unit_price()
        self.current_price = self.total_unit_price * UNIT_TO_SELLING

    # this differs from update_current_price() as this adds the unit price*quantity to the bundle price,
    # only if the offer was different from the last time the ucrrent price was calculated
    def update_current_price_diff(self,difference ):
        for item in difference:
            self.current_price -= difference[item] * self.bundle[item].unit_price*UNIT_TO_SELLING

    def update_quantity(self,products):
        # 'difference' tracks the difference in quantities between offers in order to more accurately determine a new current price
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

    # checks if the current price can be reduced
    def is_profitable(self):
        return self.current_price > self.total_unit_price

    # if a reduction in price is profitable, reduce the current price by 20% or choose the minimum price (self.total_unit_price)
    def reduce_price(self):
        if self.is_profitable():
            self.current_price =max(self.current_price * 0.80 , self.total_unit_price)

    # Resents the price and quantity back to 0
    # This should be called after we recognize that a sale has been made either by either agent
    def clear_bundle(self):
        self.current_price = 0
        for item in self.bundle:
            self.bundle[item].quantity = 0

    # ex) I can offer you 2 eggs, 3 cups of milk, for $10.57
    # Note: This does function does not print the string. It returns it
    # Usage: print(bundle.to_string())
    def to_string(self):
        string = "I can offer you "
        for item in self.bundle:
            if self.bundle[item].quantity > 0:
                string += str(self.bundle[item].quantity)
                string += " "
                if (item != "egg"): # accounts for possible mistakes such as "2 each of eggs". Instead skip unit and 'of' for eggs
                    string += self.bundle[item].unit
                    string += " of "
                string += item
                if(item == "egg" and self.bundle[item].quantity>1): # accounts for "1 egg vs 2 eggs"
                    string += "s"
                string += ", "
        string += "for $"
        string += str(round(self.current_price,2)) # makes sure currency is displayed as at most 2 digits past the decimal point
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
