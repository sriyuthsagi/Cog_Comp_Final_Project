import watson_assistant


class Agent:

    def __init__(self, name, room_num):
        self.my_name = name
        self.room_num = room_num
        
        self.user_intent = ""
        self.user_price = -1
        self.opponent_intent = ""
        self.opponent_price = -1
        
        
        self.firstRound = True
        self.hasSpokenAlreadyThisRound = False
    
    
    
    def setUtility(self, util):
        
        self.egg_unit = util["utilityParameters"]["egg"]["unit"]
        self.flour_unit = util["utilityParameters"]["flour"]["unit"]
        self.sugar_unit = util["utilityParameters"]["sugar"]["unit"]
        self.milk_unit = util["utilityParameters"]["milk"]["unit"]
        self.chocolate_unit = util["utilityParameters"]["chocolate"]["unit"]
        self.blueberry_unit = util["utilityParameters"]["blueberry"]["unit"]
        self.vanilla_unit = util["utilityParameters"]["vanilla"]["unit"]
        
        self.egg_cost = util["utilityParameters"]["egg"]["parameters"]["unitcost"]
        self.flour_cost = util["utilityParameters"]["flour"]["parameters"]["unitcost"]
        self.sugar_cost = util["utilityParameters"]["sugar"]["parameters"]["unitcost"]
        self.milk_cost = util["utilityParameters"]["milk"]["parameters"]["unitcost"]
        self.chocolate_cost = util["utilityParameters"]["chocolate"]["parameters"]["unitcost"]
        self.blueberry_cost = util["utilityParameters"]["blueberry"]["parameters"]["unitcost"]
        self.vanilla_cost = util["utilityParameters"]["vanilla"]["parameters"]["unitcost"]
        








if __name__ == "__main__" :

    agent = Agent("Watson", 1001)

    # read transcript from input
    util = {"sender":"MarketPlace","msgType":"setAgentUtility","utilityParameters":{
        "egg":{"type":"unitcost","unit":"each","parameters":{"unitcost":0.45}},
        "flour":{"type":"unitcost","unit":"cup","parameters":{"unitcost":0.93}},
        "sugar":{"type":"unitcost","unit":"cup","parameters":{"unitcost":0.69}},
        "milk":{"type":"unitcost","unit":"cup","parameters":{"unitcost":0.35}},
        "chocolate":{"type":"unitcost","unit":"ounce","parameters":{"unitcost":0.34}},
        "blueberry":{"type":"unitcost","unit":"packet","parameters":{"unitcost":0.48}},
        "vanilla":{"type":"unitcost","unit":"teaspoon","parameters":{"unitcost":0.33}}}}
    agent.setUtility(util)
    print(agent.egg_unit)

    
