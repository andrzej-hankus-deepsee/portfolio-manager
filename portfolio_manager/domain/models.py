from pydantic import BaseModel


class Position(BaseModel):
    symbol: str
    shares: int

class Portfolio(BaseModel):
    id : int | None = None
    name: str
    cash: float
    positions: list[Position]

class Ticker(BaseModel):
    id : int | None = None
    symbol: str
    price: float