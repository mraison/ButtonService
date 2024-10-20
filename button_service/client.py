from kombu import Exchange, Producer, Connection


class RabbitClient:
    def __init__(self, url: str, routing_key: str, exchange: Exchange):
        self._url = url
        self._routing_key = routing_key
        self._exchange = exchange

    def send(self, data: dict) -> bool:
        with Connection(self._url) as conn:
            with conn.channel() as chan:
                producer = Producer(chan)
                producer.publish(
                    data,
                    exchange=self._exchange,
                    routing_key=self._routing_key,
                    declare=[self._exchange]
                )
                return True

