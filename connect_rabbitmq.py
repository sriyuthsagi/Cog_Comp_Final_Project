import pika
import json

from agent import Agent

# REMEMBER TO ASK::: msg.sender? or other?
ip = '128.113.21.86'

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host=ip,
                                       virtual_host='/',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

agen = 'Celia'
agent = Agent(agent, 1001)
to_channel = 'to-' + agent.lower

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

def callback_ag(ch, method, properties, body):
    print(" [x] Received 1 %r" % body)

    msg = json.loads(body.decode('utf8'));
    print(msg)

    if msg['msgType'] != 'startRound':
        agent.setUtility(msg)

def callback(ch, method, properties, body):
    print(" [x] Received 2 %r" % body)

    msg = json.loads(body.decode('utf8'));
    
    try:
        if msg["msgType"] == "setAgentUtility":
            agent.setUtility(msg)
        
    except:
        reply = agent.get_response(msg);
        ch.basic_publish(exchange='amq.topic', routing_key='output-gate', body=json.dumps(reply));
    
connect_to_server();

    #channel.queue_declare(queue='amq.topic')
channel.basic_consume(
    queue=to_channel, on_message_callback=callback, auto_ack=True)
channel.basic_consume(
    queue='to-agents', on_message_callback=callback, auto_ack=True)
channel.basic_consume(
    queue='offers', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
