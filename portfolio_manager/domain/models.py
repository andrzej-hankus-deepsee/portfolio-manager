from pydantic import BaseModel, Field
import datetime
from fastapi import HTTPException

class Ticker(BaseModel):
    symbol: str = Field(..., unique=True)
    price: float

class TickerRecord(BaseModel):
    symbol: str
    price: float
    time: datetime.datetime

class Position(BaseModel):
    ticker: Ticker
    shares: int
    buying_price: float

class PositionOrder(BaseModel):
    ticker: Ticker
    shares: int
    max_price: float

class Portfolio(BaseModel):
    id : int = Field(..., unique=True)
    name: str
    cash: float
    positions: list[Position]
    orders: list[PositionOrder]

    def sell(self, position: Position, shares: int) -> bool:
        if position.shares < shares:
            return False
        
        self.cash += position.ticker.price * shares
        position.shares -= shares
        if position.shares == 0:
            self.positions.remove(position)

        return True

    def create_order(self, ticker: Ticker, shares: int, max_price: float) -> bool:
        if shares * max_price > self.cash:
            return False
        
        self.cash -= shares * max_price

        order = PositionOrder(
            ticker=ticker,
            shares=shares,
            max_price=max_price
        )

        self.orders.append(order)
        if ticker.price < max_price:
            self.buy(order)
        
        return True

    def buy(self, order: PositionOrder) -> bool:
        if not order in self.orders:
            return False
        if order.ticker.price > order.max_price:
            return False

        position = Position(
            ticker=order.ticker,
            shares=order.shares,
            buying_price=order.ticker.price 
            )
        
        change = (order.max_price - order.ticker.price)*order.shares
        self.cash += change
        
        self.positions.append(position)
        
        self.orders.remove(order)
        return True