RabbitMQ Prometheus Exporter

This Python script exports RabbitMQ queue metrics to Prometheus. It connects to the RabbitMQ management HTTP API and periodically collects the following metrics for all queues in all virtual hosts (vhosts):

Total messages: The total count of messages in the queue.
Ready messages: The number of ready messages in the queue (messages that are waiting to be consumed).
Unacknowledged messages: The number of messages that have been delivered to consumers but not yet acknowledged.
These metrics are exposed as Prometheus gauges with the following labels:

host: RabbitMQ host.
vhost: RabbitMQ virtual host.
name: The name of the queue.

Requirements

Python 3.x
Prometheus Python Client (prometheus_client)
requests library
python-dotenv for loading environment variables from a .env file


Setup

1. Install Dependencies
To install the required Python libraries, you can use pip:

pip install prometheus_client requests python-dotenv
2. Create a .env File
Create a .env file in the root directory of the project and add the following environment variables to configure the RabbitMQ connection:

RABBITMQ_HOST=Your_Rabbitmq_url
RABBITMQ_USER=Your_Rabbitmq_user
RABBITMQ_PASSWORD=your_rabbitmq_password

3. Run the Script
Run the script to start the Prometheus exporter:

python rabbitmq_exporter.py
By default, the exporter will start an HTTP server on port 8000 to expose the metrics. Prometheus can scrape these metrics by configuring the exporter as a scrape target.


4. View Metrics
Once the exporter is running, you can view the metrics by visiting:

http://<hostname or ip>:8000/metrics
Prometheus will now periodically scrape these metrics from your exporter.
