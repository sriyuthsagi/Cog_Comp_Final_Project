import watson_assistant
import parse_sentence


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

    def get_response(self,msg):

        reply = {}
        reply['inReplyTo'] = ''
        reply['sender'] = self.my_name
        reply['transcript'] = "Please buy from me. " #this shouldnt be said. only here as emergency backup
        reply['room'] = self.room_num

        sender = "User"
        if (sender == None or sender == "null"): sender = "User"
        transcript = ''
        addressee = 'Celia'

        my_name = self.my_name
        if my_name == "Watson":
            other_name = "Celia"
        else:
            other_name = "Watson"

        # Determine whether we will respond to this message
        willRespond = False;
        if addressee == my_name:
            willRespond = True;
            print("Will respond. Has been addressed directly.")
        elif addressee == other_name:
            willRespond = False;
            print("Will not respond. Other agent has been addressed directly.")
        else:
            if sender == my_name:
                print("Will not respond. Is own message.")
                willRespond = False;
            else:
                print("Will respond. Is not addressed to anyone in particular.")
                willRespond = True;

        # Store data to preserve between passes
        if sender == my_name:
          print("Message from self") #just here as a placeholder really
          reply["transcript"] = ""
        elif sender == "User":
          # get opponent_intent and opponent_price
          self.user_intent = watson_assistant.get_intent(transcript)
          self.hasSpokenAlreadyThisRound = False
          print("New round begin. User intent Id'd as ",self.user_intent)
          self.wanted = parse_sentence.findProduct(transcript)
          self.user_price = self.wanted["price"]
          print('user', self.user_intent)
          print(self.wanted)

          if(self.user_intent=="bargaining"):
              reply["transcript"] = "Yes I can offer you a 20 percent discount."
          if(self.user_intent=="ask_price"):
              reply["transcript"] = "The price for those items is " + random.randint(4,10) +"dollars."
          if(self.user_intent=="opponent_sale"):
              reply["transcript"] = "Hi, are there any other items you would like to buy?"
          if(self.user_intent=="product_info"):
              reply["transcript"] = "All of my products are of the highest quality."
          if(self.user_intent=="buy_product"):
              reply["transcript"] = "Okay, I can offer you this for " + random.randint(4,10) + " dollars."
          if(self.user_intent=="accept_offer"):
              reply["transcript"] = "Okay, here you go! Thanks for doing business with me."
          if(self.user_intent=="General_Greetings"):
              reply["transcript"] = "Hello! Would you like to buy anything from me today?"
          if(self.user_intent=="General_Ending"):
              reply["transcript"] = "Have a nice day."


        else:# if sender == other_name:
          # get opponent_intent and opponent_price
          self.opponent_intent = watson_assistant.get_intent(transcript)
          self.wanted = parse_sentence.findProduct(transcript)
          self.opponent_price = self.wanted["price"]
          print('user', self.opponent_intent)
          print(self.wanted)
          if(self.opponent_intent == "opponent_price"):
              reply["transcript"] = "Excuse me, I overheard that you are interested in buying ingredients. Would you like those same ingredients for "+ opponent_price*.8
        # dont respond more than once per round
        if self.hasSpokenAlreadyThisRound:
          willRespond = False
          print("Will not respond. Has already spoken in this round.")


        if willRespond:
            self.hasSpokenAlreadyThisRound = True
            #reply["transcript"] = response(self.wanted, self.intent)
        reply["transcript"] = 'I can give you 3 eggs for $5'
        print(reply)
        return reply;


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
