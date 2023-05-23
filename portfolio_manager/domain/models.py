from pydantic import BaseModel


class Position(BaseModel):
    ticker: str
    shares: float
    price: float


class Portfolio(BaseModel):
    id: int
    name: str
    cash: float
    positions: list[Position]
