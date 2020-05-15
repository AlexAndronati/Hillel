import rabbitpy
import threading

# RABBITMQ_URL = "amqp://vzfrhuaa:27Jr-CXjNQ6wuoMgo3XuW_PJAbdrREaK@whale.rmq.cloudamqp.com/vzfrhuaa"
RABBITMQ_URL = "amqp://smcxvekg:l-PiXagQVSaBkLqvm64s1vXD14qkotVZ@roedeer.rmq.cloudamqp.com/smcxvekg"


class RabbitQueue:
    def __init__(self, exchange_name, queue_name):
        self.queue_name = queue_name
        self.exchange_name = exchange_name
        self.routing_name = queue_name

        self.connection = rabbitpy.Connection(RABBITMQ_URL)
        self.channel = self.connection.channel()

        self.exchange = rabbitpy.Exchange(self.channel, self.exchange_name, durable=True)
        self.exchange.declare()

        self.queue = rabbitpy.Queue(self.channel, self.queue_name, durable=True)
        self.queue.declare()
        self.queue.bind(self.exchange, routing_key=self.routing_name)

    def publish(self, message: dict):
        message = rabbitpy.Message(self.channel, message)
        message.publish(self.exchange_name, self.routing_name)

    def consume_generator(self, threads=5):
        for m in self.queue.consume(prefetch=threads):
            yield m.json()
            m.ack()

    def count(self):
        return len(self.queue)

    def close(self):
        self.channel.close()
        self.connection.close()


def consumer(queue):
    for message in queue.consume_generator():
        print(message)


def publisher(queue, number_of_messages):
    for i in range(number_of_messages):
        queue.publish({"message": f"hi {i}"})
        print(f"publishing hi {i}")


if __name__ == '__main__':
    number_of_messages = 140
    input_q = RabbitQueue("test-exchange", "test_queue")
    output_q = RabbitQueue("test-exchange", "test_queue")

    publisher_thread = threading.Thread(target=publisher, args=(input_q, number_of_messages))
    consumer_thread = threading.Thread(target=consumer, args=(output_q,))
    consumer_thread.start()
    publisher_thread.start()

    publisher_thread.join()
    consumer_thread.join()






