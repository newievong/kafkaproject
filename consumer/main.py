from confluent_kafka import Consumer

def main():
    consumer = Consumer({'bootstrap.servers': 'kafka_broker:9092', 'group.id': 'consumer_group',
                         'auto.offset.reset': 'earliest'})
    consumer.subscribe(['wikimedia_events'])

    while True:
        message = consumer.poll(timeout = 1.0)
        if message is None:
            continue
        if message.error():
            print(f'Consumer error: {message.error()}')
        print('Received message:', message.value())

if __name__ == '__main__':
    main()

