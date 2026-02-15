import json
import os
import pika
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
QUEUE_NAME = os.getenv("QUEUE_NAME", "task_queue")


def _connection_params():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    return pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials)


def publish_message(message: dict):
    conn = pika.BlockingConnection(_connection_params())
    channel = conn.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    body = json.dumps(message)
    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=body,
        properties=pika.BasicProperties(delivery_mode=2),
    )
    conn.close()


if __name__ == "__main__":
    publish_message({"title": "Hi Platform Solutions Team", "description": "test"})
