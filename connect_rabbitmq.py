import pika
import json

from agent import Agent

# this is the ip address that rabbitmq should connect to in order to send and recv messages
ip = '128.113.21.86' # 'localhost'

# most of the following code within this file can be found the API documentation on Watson assistant
# https://www.rabbitmq.com/documentation.html
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host=ip,
                                       virtual_host='/',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Change agent_main and to_channel if the name of this agent changes
agent_main = 'Celia'
agent = Agent(agent_main, 1001)
to_channel = 'to-celia' #+ agent_main.lower()


def connect_to_server():

    channel.queue_declare(queue='to-agents')
    channel.queue_declare(queue='output-gate')
    channel.queue_declare(queue=to_channel)
    channel.queue_declare(queue='offers')

    #channel.exchange_declare(exchange='amq.topic',
                             #type='direct', durable=True)

    channel.queue_bind(exchange='amq.topic',
                       queue='to-agents')
    channel.queue_bind(exchange='amq.topic',
                       queue='output-gate')
    channel.queue_bind(exchange='amq.topic',
                       queue=to_channel)
    channel.queue_bind(exchange='amq.topic',
                       queue='offers')
    return channel

def callback(ch, method, properties, body):
    print(" [x] Received 2 %r" % body)

    msg = json.loads(body.decode('utf8'));

    try:
        # Set the utilities and create a bundle if we recv the correct json
        if msg["msgType"] == "setAgentUtility":
            agent.setUtility(msg)

    except:
        # otherwise, we recvd a normal message and we should generate a response depending on the input (agent.py)
        reply = agent.get_response(msg);
        ch.basic_publish(exchange='amq.topic', routing_key='output-gate', body=json.dumps(reply));
        print('edvc')

connect_to_server()

# consume on these 3 channels to recv all possible input

# This is consuming on to-watson or to-celia. This is where we get the utility function
channel.basic_consume(
    queue=to_channel, on_message_callback=callback, auto_ack=True)
# This is consuming on to-agents. We get all messages here. This is where we get the input from the normal conversation
channel.basic_consume(
    queue='to-agents', on_message_callback=callback, auto_ack=True)
# This is consuming on offers. This is where we recv the accept, offer, and confirm jsons
channel.basic_consume(
    queue='offers', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
