# import mqProducerInterface # type: ignore
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.m_connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.m_channel = self.m_connection.channel()

        # Create the exchange if not already present
        # self.m_channel.exchange_declare(self.m_exchange_name)
        self.m_channel.exchange_declare(
            exchange=self.exchange_name, exchange_type="Topic"
        )

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.m_channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message,
        )

        print(" [x] Sent Orders")

    def __del__(self) -> None:
        print(f"Closing RMQ connection on destruction")
        self.m_channel.close()
        self.m_connection.close()