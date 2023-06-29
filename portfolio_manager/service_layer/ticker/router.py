import aio_pika
import asyncio
import sys
import json

from fastapi import APIRouter, Depends, HTTPException

from portfolio_manager.service_layer.ticker.schemas import TickerSchema
from portfolio_manager.shared.schemas import SuccessSchema
from portfolio_manager.bootstrap import get_bootstrap, Bootstrap

router = APIRouter()

@router.post("/",status_code=201)
async def create_ticker(
    ticker: TickerSchema, 
    bootstrap: Bootstrap = Depends(get_bootstrap),
) -> SuccessSchema:
    result = await bootstrap.ticker_repository.create_one(ticker=ticker)
    if not result:
        raise HTTPException(status_code=409, detail="Ticker already exists")
    return {"success": result}


@router.patch("/",status_code=201)
async def update_ticker(
    ticker: TickerSchema, 
    bootstrap: Bootstrap = Depends(get_bootstrap),
) -> SuccessSchema:
    result = await bootstrap.ticker_repository.update_one(ticker=ticker)
    if not result:
        raise HTTPException(status_code=404, detail="Ticker not found")
    return {"success": result}


async def start_ticker_message_queue():
    bootstrap = get_bootstrap()

    async def connect_to_rabbit_mq():
        tries = 10
        interval = 1 
        for _ in range(tries):
            try:
                return await aio_pika.connect_robust("amqp://guest:guest@message_queue/")
            except aio_pika.exceptions.AMQPConnectionError:
                await asyncio.sleep(interval)
    
    async def on_message(message: aio_pika.IncomingMessage):
        async with message.process():
            data = json.loads(message.body)
            print("Received data:", data)
            sys.stdout.flush()
            sys.stderr.flush()

            for key, value in data.items():
                ticker = TickerSchema(symbol=key, price=value)
                await bootstrap.ticker_repository.update_one(ticker=ticker)
                await bootstrap.portfolio_repository.respond_to_price_change(ticker=ticker)
        
    connection = await connect_to_rabbit_mq()

    print(connection)
    
    channel = await connection.channel()
    queue = await channel.declare_queue("tick_update")

    await queue.consume(on_message)
    print("Connected to RabbitMQ")