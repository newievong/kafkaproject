from confluent_kafka import Producer
import requests
import time

URL = 'https://stream.wikimedia.org/v2/stream/recentchange'
def main():
    time.sleep(2.0)
    producer = Producer({'bootstrap.servers': 'kafka_broker:9092'})
    message = requests.get(URL).text
    producer.poll(0)
    producer.produce('wikimedia_events', message)
    producer.flush()

if __name__ == '__main__':
    main()

