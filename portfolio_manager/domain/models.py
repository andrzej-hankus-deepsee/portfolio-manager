from pydantic import BaseModel, Field

class Ticker(BaseModel):
    symbol: str = Field(..., unique=True)
    price: float

class Position(BaseModel):
    ticker: Ticker
    shares: int

class Portfolio(BaseModel):
    id : int = Field(..., unique=True)
    name: str
    cash: float
    positions: list[Position]

