from pydantic import BaseModel


class Position(BaseModel):
    symbol: str
    shares: int
    price: float


class Portfolio(BaseModel):
    id : int | None = None
    name: str
    cash: float
    positions: list[Position]
