# connects to watson 

from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_key = "4vNMoOfmBvKK8AQakpuTqtMQoD1EAyvFXtP9tX15hqYK"
assistant_id = "d86dad12-dfff-48e6-82b7-cbd1efc44426"

# Set up Assistant service.
authenticator = IAMAuthenticator(api_key) # replace with API key
service = AssistantV2(
    version = '2019-02-28',
    authenticator = authenticator
)

service.set_service_url('https://gateway.watsonplatform.net/assistant/api/v2/assistants/d86dad12-dfff-48e6-82b7-cbd1efc44426/sessions')

def get_intent(transcript):

  # Create session.
  session_id = service.create_session(
      assistant_id = assistant_id
  ).get_result()['session_id']

  # Initialize message_input with transcript (input text)
  message_input = {
    'message_type:': 'text',
    'text': transcript
    }

  
  # Start conversation with empty message.
  response = service.message(
      assistant_id,
      session_id,
      input = message_input
  ).get_result()

  intent = ""
  # If an intent was detected, set it to be returned.
  if response['output']['intents']:
      intent = response['output']['intents'][0]['intent']
  
  # Print the output from dialog, if any. Supports only a single
  # text response.
  #if response['output']['generic']:
  #    if response['output']['generic'][0]['response_type'] == 'text':
  #        print(response['output']['generic'][0]['text'])

  # We're done, so we delete the session.
  service.delete_session(
      assistant_id = assistant_id,
      session_id = session_id
  )
  
  # Return the intent 
  return intent

# for testing
if __name__ == "__main__" :

    # read transcript from input
    user_input = input('>> ')
    
    # get intent
    print(get_intent(user_input))
    

####################################
    
    
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import rabbitmq

"""
# how to send messages to code
# make sure input is in JSON format
http://localhost:15672/#/exchanges/%2F/amq.topic
"""
# global variables

# name of self
# either 'Watson' or 'Celia'
AGENT_NAME = 'Celia'
api_key = '4vNMoOfmBvKK8AQakpuTqtMQoD1EAyvFXtP9tX15hqYK'
assist_id = 'd86dad12-dfff-48e6-82b7-cbd1efc44426'
# create an empty dictionary for the sessionID
sessionID = dict()
authenticator = IAMAuthenticator(api_key)
service = AssistantV2(
    version='2019-02-28',
    authenticator = authenticator
)

service.set_service_url('https://gateway.watsonplatform.net/assistant/api')

sessionID = service.create_session(
    assistant_id=assist_id
).get_result()


def main():
    rabbitmq.connect_to_server()
    rabbitmq.receive()
    # https://www.cloudamqp.com/blog/2015-05-21-part2-3-rabbitmq-for-beginners_example-and-sample-code-python.html

"""
WATSON CODE GOES HERE
Get the response from Watson Assistant Chatbot
"""
def agent_code(body):
    # Send user input to an assistant and receive a response.
    response = service.message(
        assistant_id=assist_id,
        session_id=sessionID["session_id"],
        input={
            'message_type': 'text',
            'text': body['transcript']
        }
    ).get_result()

    """
    OUTPUT:
    Exchange = amq.topic
    Topic/Queue/Channel =  output-gate
    Format: JSON
    {
        “inReplyTo”: use the currentState variable from input if you are replying to that message,
        “sender”: Watson | Celia (case sensitive, use this as global variable so your agent can be quickly changed)
        “transcript” Your text output to be spoken,
        “room”: 1001 (preset do not change)
    }
    """

    output = dict()
    output["inReplyTo"] = body['currentState']
    output["sender"] = AGENT_NAME
    output["transcript"] = response['output']['generic'][0]['text']
    output["room"] = 1001

    rabbitmq.send_to_server(rabbitmq.channel, output)

"""
This function will be run as soon as a message is received.
Sends the message received from rabbitmq to Watson Assistant Chatbot
"""
def on_message(ch, method, properties, body):

    """
    INPUT
    Format: JSON
    {
        "sender": "Watson|Celia|User",
        "transcript": "I want to buy water",
        "addressee": "Celia|Watson|null",
        "currentState": "(use this as is and pass this on if you are replying to this message)"
    }
    """
    print("RECEIVED:")
    json_body = json.loads(body.decode('utf8'))
    print(json.dumps(json_body, indent=2))

    # only respond if I didn't just send a message (I can't respond to myself)
    # I'm not sure if this is already handled by the manager in Rahul's code
    if (json_body["sender"] != AGENT_NAME):
        agent_code(json_body)


if __name__ == "__main__":
    main()
