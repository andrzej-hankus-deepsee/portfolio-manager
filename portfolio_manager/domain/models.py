from pydantic import BaseModel, Field
import datetime

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
