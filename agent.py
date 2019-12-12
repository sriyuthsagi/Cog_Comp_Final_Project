import watson_assistant
import parse_sentence
import basic_classes

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

        self.egg_unit = util["utilityParameters"]["utility"]["egg"]["unit"]
        self.flour_unit = util["utilityParameters"]["utility"]["flour"]["unit"]
        self.sugar_unit = util["utilityParameters"]["utility"]["sugar"]["unit"]
        self.milk_unit = util["utilityParameters"]["utility"]["milk"]["unit"]
        self.chocolate_unit = util["utilityParameters"]["utility"]["chocolate"]["unit"]
        self.blueberry_unit = util["utilityParameters"]["utility"]["blueberry"]["unit"]
        self.vanilla_unit = util["utilityParameters"]["utility"]["vanilla"]["unit"]

        self.egg_cost = util["utilityParameters"]["utility"]["egg"]["parameters"]["unitcost"]
        self.flour_cost = util["utilityParameters"]["utility"]["flour"]["parameters"]["unitcost"]
        self.sugar_cost = util["utilityParameters"]["utility"]["sugar"]["parameters"]["unitcost"]
        self.milk_cost = util["utilityParameters"]["utility"]["milk"]["parameters"]["unitcost"]
        self.chocolate_cost = util["utilityParameters"]["utility"]["chocolate"]["parameters"]["unitcost"]
        self.blueberry_cost = util["utilityParameters"]["utility"]["blueberry"]["parameters"]["unitcost"]
        self.vanilla_cost = util["utilityParameters"]["utility"]["vanilla"]["parameters"]["unitcost"]

        # create a bundle and Initialize utlities
        self.offer = basic_classes.Bundle(self.egg_cost, self.flour_cost, self.milk_cost, self.sugar_cost, self.chocolate_cost, self.vanilla_cost, self.blueberry_cost,\
        self.egg_unit, self.flour_unit, self.milk_unit, self.sugar_unit, self.chocolate_unit, self.vanilla_unit, self.blueberry_unit)

    def get_response(self,msg):

        # msg is the input
        # reply is the output

        reply = {}
        reply['inReplyTo'] = ''
        reply['sender'] = self.my_name
        reply['transcript'] = "" #this shouldnt be said. only here as emergency backup
        reply['room'] = self.room_num

        transcript = msg['transcript']

        my_name = self.my_name
        if my_name == "Watson":
            other_name = "Celia"
        else:
            other_name = "Watson"

        if my_name in transcript:
            sender = 'User'
            receivee = my_name
        elif other_name in transcript:
            sender = 'User'
            receivee = 'Other'
        else: # there is no @. This means that an agent is talking
            try:
                if msg['sender'] == my_name: # our agent is talking
                    sender = my_name
                else: # the other agent is talking
                    sender = 'Other'
                receivee = 'User'
            except:
                sender = 'Other'
                receivee = msg['sender']

        if sender == 'User':
            self.user_intent = watson_assistant.get_intent(transcript)

        parse = parse_sentence.findProduct(transcript)
        products = parse[0]
        price = parse[1]

        already_reduced_price = False
        print(products)
        # This updates the quantity and the unit/current prices
        self.offer.update_quantity(products)
        if price != -1:
            # if we're given a price, reduce our current price by 20%
            if sender == 'User' or sender == 'Other':
                self.offer.reduce_price()
                already_reduced_price = True
            # else, use the unit price * 3 as our current price

        # Store data to preserve between passes
        if sender == my_name:
          print("Message from self") #just here as a placeholder really
          reply["transcript"] = ""
        elif sender == "User" or sender == 'Other':
          # get opponent_intent and opponent_price

          reply["transcript"] = self.offer.to_string()

          if(self.user_intent=="bargaining"):
              if not already_reduced_price:
                  self.offer.reduce_price()
              reply["transcript"] = self.offer.to_string()
          # if(self.user_intent=="ask_price"):
          #     reply["transcript"] = "The price for those items is " + self.offer.current_price +"dollars."
          # if(self.user_intent=="opponent_sale"):
          #     reply["transcript"] = "Hi, are there any other items you would like to buy?"
          if(self.user_intent=="product_info"):
              reply["transcript"] = "All of my products are of the highest quality."
          # if(self.user_intent=="buy_product"):
          #     reply["transcript"] = "Okay, I can offer you this for " + self.offer.current_price + " dollars."
          if(self.user_intent=="accept_offer"):
              reply["transcript"] = "Okay, here you go! Thanks for doing business with me."
              self.offer.clear_bundle()
          if(self.user_intent=="General_Greetings"):
              reply["transcript"] = "Hello! Would you like to buy anything from me today?"
          if(self.user_intent=="General_Ending"):
              reply["transcript"] = "Have a nice day."


        # else:# if sender == other_name:
        #   # get opponent_intent and opponent_price
        #
        #   if(self.opponent_intent == "opponent_price"):
        #       reply["transcript"] = "Excuse me, I overheard that you are interested in buying ingredients. Would you like those same ingredients for "+ opponent_price*.8
        #

        return reply;


if __name__ == "__main__" :

    agent = Agent("Watson", 1001)

    # read transcript from input
    util  = {"sender":"MarketPlace","msgType":"setAgentUtility","utilityParameters":{
    "currencyUnit":"USD","utility":{
    "egg":{"type":"unitcost","unit":"each","parameters":{"unitcost":0.29}},
    "flour":{"type":"unitcost","unit":"cup","parameters":{"unitcost":0.66}},
    "sugar":{"type":"unitcost","unit":"cup","parameters":{"unitcost":0.63}},
    "milk":{"type":"unitcost","unit":"cup","parameters":{"unitcost":0.26}},
    "chocolate":{"type":"unitcost","unit":"ounce","parameters":{"unitcost":0.32}},
    "blueberry":{"type":"unitcost","unit":"packet","parameters":{"unitcost":0.49}},
    "vanilla":{"type":"unitcost","unit":"teaspoon","parameters":{"unitcost":0.21}}}}}
    agent.setUtility(util)
    sample = {"transcript":"@Watson I would like to buy 12 cups of flour and 3 cups of milk for $2","currentState":{"conversation_state_id":"sNormOn","conversation_last_transition_id":"t0","conversation_turn_id":52}}
    print(agent.get_response(sample))
    sample = {"transcript":"@Watson I would like to buy 12 cups of flour and 3 cups of milk for $2","currentState":{"conversation_state_id":"sNormOn","conversation_last_transition_id":"t0","conversation_turn_id":52}}
    print(agent.get_response(sample))
    sample = {"transcript":"@Watson I would like to buy 12 cups of flour and 3 cups of milk for $2","currentState":{"conversation_state_id":"sNormOn","conversation_last_transition_id":"t0","conversation_turn_id":52}}
    print(agent.get_response(sample))
    sample = {"transcript":"@Watson I would like to buy 12 cups of flour and 3 cups of milk and 2 cups of sugar","currentState":{"conversation_state_id":"sNormOn","conversation_last_transition_id":"t0","conversation_turn_id":52}}
    print(agent.get_response(sample))
    sample = {"transcript":"@Watson I would like to buy 12 cups of flour and 3 cups of milk and 2 cups of sugar for $2","currentState":{"conversation_state_id":"sNormOn","conversation_last_transition_id":"t0","conversation_turn_id":52}}
    print(agent.get_response(sample))
    sample = {"transcript":"@Watson Hello","currentState":{"conversation_state_id":"sNormOn","conversation_last_transition_id":"t0","conversation_turn_id":52}}
    print(agent.get_response(sample))
    # sample = {"transcript":"@Watson I would like to buy 2 cups of sugar","currentState":{"conversation_state_id":"sNormOn","conversation_last_transition_id":"t0","conversation_turn_id":52}}
    # print(agent.get_response(sample))
    # sample = {"transcript":"@Watson I would like to buy 0 cups of sugar","currentState":{"conversation_state_id":"sNormOn","conversation_last_transition_id":"t0","conversation_turn_id":52}}
    # print(agent.get_response(sample))
    # sample = {"transcript":"@Watson How much for 12 cups of flour?","currentState":{"conversation_state_id":"sNormOn","conversation_last_transition_id":"t0","conversation_turn_id":52}}
    # print(agent.get_response(sample))
