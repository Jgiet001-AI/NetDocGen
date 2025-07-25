import asyncio
import json
import logging
from typing import Callable, Dict, Any
import aio_pika
from aio_pika import ExchangeType

logger = logging.getLogger(__name__)

class MessageQueue:
    """RabbitMQ message queue wrapper for inter-service communication."""
    
    def __init__(self, rabbitmq_url: str):
        self.url = rabbitmq_url
        self.connection = None
        self.channel = None
        self.exchange = None
        
    async def connect(self):
        """Establish connection to RabbitMQ."""
        self.connection = await aio_pika.connect_robust(self.url)
        self.channel = await self.connection.channel()
        
        # Declare main exchange
        self.exchange = await self.channel.declare_exchange(
            "netdocgen",
            ExchangeType.TOPIC,
            durable=True
        )
        
    async def disconnect(self):
        """Close connection to RabbitMQ."""
        if self.connection:
            await self.connection.close()
    
    async def publish(self, routing_key: str, message: Dict[str, Any]):
        """
        Publish a message to the queue.
        
        Args:
            routing_key: Routing key for the message
            message: Message data as dictionary
        """
        if not self.channel:
            await self.connect()
            
        await self.exchange.publish(
            aio_pika.Message(
                body=json.dumps(message).encode(),
                content_type="application/json"
            ),
            routing_key=routing_key
        )
        logger.info(f"Published message to {routing_key}")
    
    async def consume(self, queue_name: str, routing_key: str, callback: Callable):
        """
        Consume messages from a queue.
        
        Args:
            queue_name: Name of the queue
            routing_key: Routing key pattern to bind
            callback: Async callback function to process messages
        """
        if not self.channel:
            await self.connect()
            
        # Declare queue
        queue = await self.channel.declare_queue(queue_name, durable=True)
        await queue.bind(self.exchange, routing_key)
        
        async def process_message(message: aio_pika.IncomingMessage):
            async with message.process():
                try:
                    data = json.loads(message.body.decode())
                    await callback(data)
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    # Message will be requeued on exception
                    raise
        
        await queue.consume(process_message)
        logger.info(f"Started consuming from {queue_name} with routing key {routing_key}")

# Message routing keys
class RoutingKeys:
    PARSE_VISIO = "document.parse.visio"
    GENERATE_DOC = "document.generate"
    PARSE_COMPLETE = "document.parse.complete"
    GENERATE_COMPLETE = "document.generate.complete"