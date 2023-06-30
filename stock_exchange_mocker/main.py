from random import uniform

import string
import pika
from time import sleep 
import json

RABBITMQ_HOST = 'message_queue'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'
RABBITMQ_QUEUE = 'tick_update'

# Generate a random message
def generate_random_message():
    while True:
        random_value = round(uniform(2.5, 10.0), 2)
        yield json.dumps({"APPL": random_value})
        random_value = round(uniform(0.5, 6), 2)
        yield json.dumps({"CMG": random_value})

def connect_to_rabbit_mq(parameters):
    tries = 10
    interval = 1 
    for _ in range(tries):
        try:
            return pika.BlockingConnection(parameters)
        except pika.exceptions.AMQPConnectionError:
            sleep(interval)
            

# Connect to RabbitMQ and send random messages
def send_random_messages():
    # Create a connection to RabbitMQ
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials)

    
    value_generator = generate_random_message()
    interval = 1.5
    while True:
        connection = connect_to_rabbit_mq(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_QUEUE)

        message = next(value_generator)

        channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=message)
        print(f"Sent message: {message}", flush=True)
        connection.close()
        sleep(interval)

    # Close the connection

# Start sending random messages
send_random_messages()
