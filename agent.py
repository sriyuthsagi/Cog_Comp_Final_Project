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
        
    def get_response(self,msg):
          
        reply = {}
        reply['inReplyTo'] = msg['currentState']
        reply['sender'] = self.my_name
        reply['transcript'] = "Please buy my coffee. " #this shouldnt be said. only here as emergency backup
        reply['room'] = self.room_num
         
        sender = msg["sender"]
        if (sender == None or sender == "null"): sender = "User"
        transcript = msg["transcript"]
        addressee = msg["addressee"]
        
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
        elif sender == "User":
          # get opponent_intent and opponent_price
          self.user_intent = watson_assistant.get_intent(transcript)
          self.hasSpokenAlreadyThisRound = False
          print("New round begin. User intent Id'd as ",self.user_intent)
          self.wanted = parse_sentence.findProduct(transcript)
          self.user_price = self.wanted["price"]
        else:# if sender == other_name:
          # get opponent_intent and opponent_price
          self.opponent_intent = watson_assistant.get_intent(transcript)
          self.wanted = parse_sentence.findProduct(transcript)
          self.opponent_price = self.wanted["price"]
        
        # dont respond more than once per round
        if self.hasSpokenAlreadyThisRound:
          willRespond = False
          print("Will not respond. Has already spoken in this round.")
        
        
        if willRespond:
            self.hasSpokenAlreadyThisRound = True
            reply["transcript"] = "This is where we need to generate the reply"

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

    
