from prometheus_client import start_http_server, Gauge
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()


RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')

metrics = {
    'messages': Gauge('rabbitmq_individual_queue_messages', 'Total messages', ['host', 'vhost', 'name']),
    'messages_ready': Gauge('rabbitmq_individual_queue_messages_ready', 'Ready messages', ['host', 'vhost', 'name']),
    'messages_unacknowledged': Gauge('rabbitmq_individual_queue_messages_unacknowledged', 'Unacknowledged messages', ['host', 'vhost', 'name'])
}

def fetch_data():
    url = f"http://{RABBITMQ_HOST}:15672/api/queues"
    response = requests.get(url, auth=(RABBITMQ_USER, RABBITMQ_PASSWORD))
    response.raise_for_status()
    print("successfully fetched data:", response.json())
    return response.json()

def update_metrics():
    queues = fetch_data()
    for queue in queues:
        metrics['messages'].labels(RABBITMQ_HOST, queue['vhost'], queue['name']).set(queue['messages'])
        metrics['messages_ready'].labels(RABBITMQ_HOST, queue['vhost'], queue['name']).set(queue['messages_ready'])
        metrics['messages_unacknowledged'].labels(RABBITMQ_HOST, queue['vhost'], queue['name']).set(queue['messages_unacknowledged'])

if __name__ == "__main__":

    start_http_server(8000)
    while True:
        update_metrics()
        time.sleep(15)
