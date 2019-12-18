# Cog_Comp_Final_Project

Final Project - Negotiation Competition Instructions
Contents
Scenario	1
Task	1
Rules	1
Utility Function	2
Project No. 1 (the small project NOT the final project)  Implementation Details for the previous round of negotiation competition – for reference only	2
Human participants' perspective	2
How will the competition be conducted?	3
FAQ	3
How will utilities be initialized? - JSON format to initialize utilities	4
Detailed choreography and messages	8



Scenario
The scenario played out will be that a human-participant (H) has been given a task of baking/cooking dishes. H needs to buy certain ingredients (I) to cook as many of the dishes. The caveat is that their budget is limited. They enter a shopping market where two AI Agents (A1 and A2) are embodied as humanoid avatars on the screen. The human can talk to them in a three-party conversation (H-A1-A2) so as to negotiate and get the best prices on the ingredients that need to be bought.
The human and the agents both have a sense of how much the items are worth to them (this may be different for each party). All parties want to maximize their own worth. This is calculated by utility functions and will be later described.

Task
Your agent can conversationally engage the human and the other AI agent such as to maximize its own profits (utilities). The agent that is able to make the sale and thus make the most profit wins that round of interaction.

List of ingredients with the links to the related information that you could use for the dialogue design of your agent:
•	Eggs
•	Flour
•	Milk
•	Sugar
•	Baking powder
•	Chocolate flavor
•	Vanilla flavor
•	Blueberry Flavor


Rules
1.	Your agent may describe their product as they wish, however, it must not be out of scope from the descriptions provided;
2.	Your agent can be rude but cannot swear;
3.	Your agent will be subject to norms of turn-taking in the three-party conversation. There is no penalty for not following the norms, just that the agent might be blocked from speaking if it violates the laws.
[Comment: There could be reward (as points) for following the norms.]
1.	You will be assigned either a masculine (Watson) or feminine (Celia) avatar/voice to represent your agent. Your code must accommodate both.
2.	Please do not spam the system with too many messages per second.
3.	You may describe your product in order to be convincing but please limit the description to what you see in the pages attached for each item to make your agent sound more fun and appealing. This may or may not affect who the user buys from.
4.	Send all possible responses of your agent to Rahul (divekr@rpi.edu) at least one day prior to the competition

Utility Function

When an agent completes an agreement to sell a bundle of goods (n_1, n_2, ..., n_G) for a price P_bundle, it receives a utility of P_bundle - Sum_i unitcost_i * n_i, where unitcost_i is the breakeven cost for the seller to produce a unit of item i. The distribution from which unitcost_i will be chosen will be provided beforehand to the agent developers. The random draw of unitcost_i for each item in the set {sugar, eggs, flour, milk, chocolate, vanilla, blueberries} will be made just prior to each round of negotiation, and therefore will not be known to the agent developers -- the agent will have to deal with it on the fly.

Project No. 1 (the small project NOT the final project)  Implementation Details for the previous round of negotiation competition – for reference only
Presentation: tinyurl.com/cogcomp19
Document: https://rpi.app.box.com/notes/552268467774


Human participants' perspective
•	How they could make an offer: I want (give me, or similar)...  <quantity> of <item>, <quantity> of <item>, <quantity> of <item> and <quantity> of <item>
•	They may not necessarily specify all items they need in one go.
•	They may not need all items listed in the ingredients list
•	They may already have some items and they don't need to buy it again
•	Not all items will give the human participant points.
•	Each recipe has a set quantities of items needed. If the human participant has excess items and cannot bake/cook anything with them (e.g. one leftover egg), they will not get points for it. However, you will still get points because you sold it.

How will the competition be conducted?

•	There will be 10 rounds of competitions between the two agents created by the two teams in the Cognitive Computing Class For the first 5 rounds of competitions, there will be a human player in each round and we will have 5 different players with the same utility function for human players.
[Question: Will the same human player play in all rounds?]
•	For the second 5 rounds of competitions, the same 5 players for the first 5 rounds will use a different utility functions  
•	In each round, the human player and the agents would like to make the highest utility based on the utility functions given to them
•	You will be given parameters for utility functions before each round
•	The results of the competition will be based on the total utility an agent gains in the total 10 rounds of competition

FAQ

1.	How will I know if my agents response was accepted
1.	Analogous to how one knows that they have successfully spoken if they can hear themselves, if the agent receives its own message back as an input, you can consider that the message was received.
2.	What units would be considered to buy items?
o	_ eggs
o	_ cups flour
o	_ cups milk
o	_ cups sugar
o	_ packets flavor
3.	Will the utility functions be provided as a code so as the agent developers can automatically calculate it for themselves?
o	The equation will be given to you. The code corresponding would be a line. We can help you with that if you need it. But we'd like you to think about the equation so you can manipulate your bid to your best benefit.
How will utilities be initialized? - JSON format to initialize utilities
You will receive a JSON (like below) on a RabbitMQ queue like 'to-<agent_name>'. E.g. if you were Celia, you'd receive it on 'to-celia' or if you are watson, you'd receive it on 'to-watson'

{
   "sender":"MarketPlace",
   "msgType":"setAgentUtility",
   "utilityParameters":{
      "egg":{
         "type":"unitcost",
         "unit":"each",
         "parameters":{
            "unitcost":0.45
         }
      },
      "flour":{
         "type":"unitcost",
         "unit":"cup",
         "parameters":{
            "unitcost":0.93
         }
      },
      "sugar":{
         "type":"unitcost",
         "unit":"cup",
         "parameters":{
            "unitcost":0.69
         }
      },
      "milk":{
         "type":"unitcost",
         "unit":"cup",
         "parameters":{
            "unitcost":0.35
         }
      },
      "chocolate":{
         "type":"unitcost",
         "unit":"ounce",
         "parameters":{
            "unitcost":0.34
         }
      },
      "blueberry":{
         "type":"unitcost",
         "unit":"packet",
         "parameters":{
            "unitcost":0.48
         }
      },
      "vanilla":{
         "type":"unitcost",
         "unit":"teaspoon",
         "parameters":{
            "unitcost":0.33
         }
      }
   }
}

This utility will be drawn from the following distribution; the unitcost parameters are drawn uniformly from the indicated ranges.

{
  "currencyUnit": "USD",
  "distribution": {
    "egg": {
      "type": "unitcost",
      "unit": "each",
      "parameters": {
        "unitcost": [0.25, 0.50]
      }
    },
    "flour": {
      "type": "unitcost",
      "unit": "cup",
      "parameters": {
        "unitcost": [0.50, 1.00]
      }
    },
    "sugar": {
      "type": "unitcost",
      "unit": "cup",
      "parameters": {
        "unitcost": [0.50, 1.00]
      }
    },
    "milk": {
      "type": "unitcost",
      "unit": "cup",
      "parameters": {
        "unitcost": [0.20, 0.40]
      }
    },
    "chocolate": {
      "type": "unitcost",
      "unit": "ounce",
      "parameters": {
        "unitcost": [0.20, 0.40]
      }
    },
    "blueberry": {
      "type": "unitcost",
      "unit": "packet",
      "parameters": {
        "unitcost": [0.25, 0.50]
      }
    },
    "vanilla": {
      "type": "unitcost",
      "unit": "teaspoon",
      "parameters": {
        "unitcost": [0.20, 0.40]
      }
    }
  }
}

It may be helpful to know the distributions from which the human's utility for cake, pancakes, and extra flavorings (chocolate, vanilla, and blueberries). Again, the ranges describe uniform distributions from which the various parameters are drawn. Specifically, the value of a plain cake is drawn uniformly between 15 and 30. Suppose that the supplement parameters for chocolate are set to minQuantity = 3, maxQuantity = 6, minValue = 2 and maxValue = 8. Then, to get extra credit for chocolate, there must be at least 3 ounces of chocolate (in which case the extra value is 2) and at most 6 ounces of chocolate (in which case the extra value is 8). If 4 ounces are added, then the extra value is obtained by linear interpolation, i.e. the extra value = 2 + (4-3)/(6-3) * (8-2) = 4.

{
  "currencyUnit": "USD",
  "distribution": {
    "cake": {
      "type": "unitvaluePlusSupplement",
      "unit": "each",
      "parameters": {
        "unitvalue": [10,20],
        "supplement": {
          "chocolate": {
            "type": "trapezoid",
            "unit": "ounce",
            "parameters": {
              "minQuantity": [3,3],
              "maxQuantity": [6,6],
              "minValue": [2, 4],
              "maxValue": [4, 8]
            }
          },
          "vanilla": {
            "type": "trapezoid",
            "unit": "teaspoon",
            "parameters": {
              "minQuantity": [2,2],
              "maxQuantity": [4,4],
              "minValue": [2, 4],
              "maxValue": [4, 8]
            }
          }
        }
      }
    },
    "pancake": {
      "type": "unitvaluePlusSupplement",
      "unitvalue": "each",
      "parameters": {
        "unitcost": [10,20],
        "supplement": {
          "chocolate": {
            "type": "trapezoid",
            "unit": "ounce",
            "parameters": {
              "minQuantity": [3,3],
              "maxQuantity": [6,6],
              "minValue": [2, 4],
              "maxValue": [4, 8]
            }
          },
          "blueberry": {
            "type": "trapezoid",
            "unit": "packet",
            "parameters": {
              "minQuantity": [1,1],
              "maxQuantity": [3,3],
              "minValue": [2, 4],
              "maxValue": [4, 8]
            }
          }
        }
      }
    }
  }
}

Also of potential interest are the ingredients required to make a plain (unflavored) cake and pancake, which are described as follows:

{
  "cake": {
    "egg": 2,
    "flour": 2,
    "milk": 1,
    "sugar": 1
  },
  "pancake": {
    "egg": 1,
    "flour": 2,
    "milk": 2
  }
}

Detailed choreography and messages

Note: make sure that we record all messages sent by MarketManager, agents, and humans.

Prior to all rounds:
1.	Open Market Manager to generate IDs for Humans and Agents:

2. Call anac-utility to generate 10 agent utilities and 2 human utilities, and permute them to determine in advance which utilities will be used for which rounds.
1.	Both agents are using the same set of 10 agent utility functions, and use the functions in a random order for the rounds
2.	All humans complete a round with human utility function 1, then all humans complete a round with human utility function 2
3. Populate the Market Manager interface of round permutations:


For each round:
1.	Click on "start round" button
2.	Send utility functions to agents using the setAgentUtility message (see above)
1.	Give agents 30 second "warm-up" phase
2.	include timestamp in setAgentUtility
3.	After warm-up phase, send message to start round:
{
  "msgType": "startRound",
  "roundNumber": 1,
  "roundDuration": 600,
  "timestamp": "<time>"
}
sent to the to-celia and to-watson topics

4. Mid-round, when an agent has made an offer (ex: agent has offered 2 pieces of chocolate for $5), then
human facilitator will keep track of offers being made and countered. Once an offer is accepted is, facilitator records this information manually.
After offer is accepted:
1.	Update Human Assistant UI is updated with:
1.	ingredients purchased
2.	deduct money spent
2.	Send to agents:
{
    “msgType”: “confirm”,
    "price": 5,
    “quantities”: {
        “Eggs”: 1,
        “Flour”: 2,
    }
    “addressee”: "human1"
}

5. At end of the round (roundDuration elapsed), send message:
{
    "msgType": "endRound",
    "timestamp": "<time>"
}
and any on-going offers are dropped. And human now gets 2 minutes to combine ingredients as they want.

6. At end of 2 minutes, scores are calculated for agents and humans and displayed appropriately.


------

Offer and acceptance messages will be sent on the offers topic

Offers from human or agents look like:
{
    “msgType”: “offer”,
    "price": 5,
    “quantities”: {
        “Eggs”: 1,
        “Flour”: 2
    }
    “addressee”: "human1"
}

Acceptances look like:
{
    “msgType”: “accept”,
    "price": 5,
    “quantities”: {
        “Eggs”: 1,
        “Flour”: 2,
    }
    “addressee”: "human1"
}

Confirmation looks like:
{
    “msgType”: “confirm”,
    "price": 5,
    “quantities”: {
        “Eggs”: 1,
        “Flour”: 2,
    }
    “addressee”: "human1"
}
