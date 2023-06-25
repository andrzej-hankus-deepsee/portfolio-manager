from fastapi import FastAPI, Depends
import aio_pika
import asyncio
import sys

from portfolio_manager.service_layer.portfolio.router import router as portfolios_router
from portfolio_manager.service_layer.ticker.router import router as tickers_router
from portfolio_manager.bootstrap import get_bootstrap, Bootstrap

API_PREFIX = "/api/v1"

api = FastAPI(
    title="Portfolio Manager API",
    version="1.0.0",
    docs_url="/api/v1/docs",
    redoc_url=None,
)

api.include_router(tickers_router, prefix=f"{API_PREFIX}/tickers", tags=["tickers"])
api.include_router(portfolios_router, prefix=f"{API_PREFIX}/portfolios", tags=["portfolios"])

async def connect_to_rabbit_mq():
    return await aio_pika.connect_robust("amqp://guest:guest@message_queue/")

@api.on_event("startup")
async def startup_event():
    # Establish a connection to RabbitMQ
    try:
        connection = await connect_to_rabbit_mq()
    except:
        await asyncio.sleep(15)
        connection = await connect_to_rabbit_mq()

    print(connection)
    
    # Create a channel
    channel = await connection.channel()
    
    # Declare a queue
    queue = await channel.declare_queue("my_queue")
    
    # Define the callback function to process incoming messages
    async def on_message(message: aio_pika.IncomingMessage, bootstrap: Bootstrap = Depends(get_bootstrap)):
        async with message.process():
            print("Received message:", message.body)
        
        sys.stdout.flush()
        sys.stderr.flush()
    
    # Set the callback function for consuming messages
    await queue.consume(on_message)
    print("Connected to RabbitMQ")