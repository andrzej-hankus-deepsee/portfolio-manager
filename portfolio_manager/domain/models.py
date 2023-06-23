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

class Portfolio(BaseModel):
    id : int = Field(..., unique=True)
    name: str
    cash: float
    positions: list[Position]

