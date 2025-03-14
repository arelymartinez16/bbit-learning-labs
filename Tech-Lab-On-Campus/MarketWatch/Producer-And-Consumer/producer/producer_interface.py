# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pika
import os


class mqProducerInterface:
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables

        # Call setupRMQConnection
        pass

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.channel = self.connection.channel()

        # Create the exchange if not already present
        exchange = self.channel.exchange_declare(exchange="Exchange Name")

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.channel.basic_publish(
            exchange="Exchange Name",
            routing_key="Routing Key",
            body=f"{message}",
        )

        # Close Channel
        self.channel.close()

        # Close Connection
        self.connection.close()